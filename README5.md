# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 314eb40a-faeb-32b0-8972-7e00cba9663b | -6.59864 | -59.1318 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d30f5eb3-391a-3ae1-881e-4273ea7e4445 | -6.72699 | -58.932 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6ac9ca54-af21-3c7e-b9b0-77990c30bd0a | -6.65425 | -56.40933 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b471bb3f-d5db-3f89-af12-60bb78817218 | -4.37035 | -47.78268 | 2026-08-07 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d34c987a-8d56-3bf2-9b3f-6c35225134d5 | -6.71205 | -58.96568 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1b4669ae-7acc-381e-bd6b-d8182c5f06ef | -4.4588 | -47.93539 | 2026-08-07 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| ec21a717-5cd2-392a-816f-21148e6962f0 | -4.27323 | -48.20803 | 2026-08-07 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8365945e-2f54-3816-ba3b-89e3deafe3a6 | -6.10151 | -55.81324 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3cefdca3-c1d4-3b88-9bcf-214b356d97f9 | -6.59723 | -59.12127 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3a7ee299-33da-37e6-9d9c-b39576f074ae | -6.64545 | -56.41058 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 248d3587-10de-3ce7-8703-a91e7a396b41 | -6.70667 | -58.9621 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 537ead93-260c-3df6-9ef4-362d4b2520cc | -4.26886 | -48.20198 | 2026-08-07 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 913671dd-d123-39c4-9342-fe0cec3673d3 | -6.8682 | -58.93867 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 29ac3f33-6db9-39c2-82a7-d5f3b1d01222 | -6.85194 | -58.96205 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30b59640-50d4-381c-996a-e3b88d43ae96 | -6.70934 | -58.94492 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6ac2efbd-948e-316e-b69a-fddb471a258e | -6.54303 | -55.15319 | 2026-08-07 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4aa981a6-2060-381c-bedd-6eed00243e51 | -6.54124 | -56.53627 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8278edff-74b6-303f-8ae7-0d53ccb80f07 | -5.98152 | -52.15211 | 2026-08-07 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0a7302f3-9397-3105-bd6e-bf9f3db65bf4 | -6.53883 | -54.92767 | 2026-08-07 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 941c727f-5ca4-3963-82ca-d2979b305e76 | -6.55795 | -56.24909 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 30e1122a-7fd2-348c-898a-2a29f541dd32 | -6.86171 | -46.03283 | 2026-08-07 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 495f0ae7-6e5f-3ab4-af76-42870883e523 | -6.8613 | -56.57447 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4758fed8-e8bf-3c84-904f-4c7ea27d7854 | -6.54691 | -55.18102 | 2026-08-07 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a5819489-97a8-31ac-ba96-8ab256e94a1b | -6.42076 | -55.79527 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9bb88142-b09f-3a70-9b4f-bc163fc40edb | -6.71749 | -58.93329 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 48954ea8-e269-3467-bb12-f738ffab9dc9 | -6.60779 | -56.34995 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42d437ad-0614-37fd-a509-efbed7b4a0c8 | -6.54366 | -56.55388 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dd0706cf-1c7b-36d3-a87d-d2e1eb8170eb | -6.85504 | -45.99047 | 2026-08-07 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 2e6af047-f812-33ba-9485-f12a6e2af4ff | -6.55036 | -56.25917 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 581480b1-4ad2-3418-885e-19a466791ad1 | -6.85868 | -58.93998 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 3632d9bf-4522-33f2-8a89-78f18488d976 | -2.08424 | -54.44284 | 2026-08-07 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9e02d5ca-baa0-37e1-bc38-6b706afa0b52 | -6.64788 | -56.42819 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2ce4e0e5-cf49-3f55-b1a7-d31221151bb4 | -6.7107 | -58.95528 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4f8b9fe5-6a8b-36ea-b1f6-d2ab307c4fb8 | -2.05745 | -59.65857 | 2026-08-07 00:35:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0eaa8e16-d06c-386b-9bbd-b32e3ae5bca4 | -6.87011 | -56.57323 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac61e5ef-6be4-3323-9bf6-cef592d4877f | -6.65303 | -56.40052 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f8feceeb-bcac-33e4-bb12-8c6be77249c7 | -7.03683 | -56.51053 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4b25a6bd-4769-3e75-9d5d-25dfd9084457 | -6.72801 | -58.58105 | 2026-08-07 00:35:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84f91d36-fd40-3541-b413-75506ea8c0e2 | -5.98358 | -52.16605 | 2026-08-07 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| f5ffdaf5-2feb-3451-8ab7-bb64d37ac118 | -6.70526 | -58.95172 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| f325f478-f3f4-3e98-aba8-f793d7ed0a01 | -6.65546 | -56.41814 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17609e75-0e19-3fa6-a2fe-fc89e30414af | -6.54914 | -56.25034 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9bd78f6-0ff9-3085-ba42-8ef797ad9001 | -6.62024 | -56.37512 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1dd6ec06-ddce-3c01-8312-ad28cc752f6d | -6.87923 | -56.50906 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0331daaf-9516-3c9e-910c-987d16e7fd68 | -6.95877 | -52.80404 | 2026-08-07 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a053c36d-c0fa-37dd-93c4-1118044a1629 | -6.53365 | -56.54632 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 52fb9d45-9c80-3be4-bd8a-aaa4cca0b874 | -6.72935 | -58.59093 | 2026-08-07 00:35:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3951abb2-fd9c-38a2-8789-242343064a9c | -6.84241 | -58.96337 | 2026-08-07 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8426f78e-868f-3f17-80d6-0fd1c967dbff | 2.75379 | -60.57675 | 2026-08-07 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0cdb6f41-b965-32cc-a0f2-a87a7202ddee | 2.52439 | -60.64803 | 2026-08-07 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| df58dbc1-54f0-3540-b735-1d05efe46113 | 1.94323 | -60.85247 | 2026-08-07 00:37:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 59894446-6d05-3f7e-85f2-6438de2ae408 | 2.523 | -60.65804 | 2026-08-07 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77d9ef9c-3cd5-39b5-ae2b-9806d66a5c1c | 2.51641 | -60.6367 | 2026-08-07 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf1e57be-2312-3e9d-b974-71d69f809409 | 2.51502 | -60.64669 | 2026-08-07 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| f346a1a5-588f-32ee-8e00-29a1389a6b30 | 1.93369 | -60.85115 | 2026-08-07 00:37:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1ee364df-dbc5-3d46-b52e-94cc8e22030e | -11.4681 | -44.5558 | 2026-08-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b36705d1-d599-38c1-973b-8a4929a8e22d | -16.1838 | -47.8783 | 2026-08-07 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 44d7a7de-79f0-3cc7-9174-78a034f2657b | -16.1833 | -47.9011 | 2026-08-07 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 579433b1-f8db-38f7-9ad6-a15d9410cfe7 | -11.1635 | -44.4838 | 2026-08-07 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 2a57f962-6402-3f55-a537-76b6e497529d | -19.7021 | -48.1336 | 2026-08-07 00:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 589b05b8-fb5c-32af-b3c4-7ca4d8ad807c | -19.7224 | -48.1291 | 2026-08-07 00:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e8d7feae-0496-30a6-b99d-8613b93f76fb | -11.4677 | -44.5791 | 2026-08-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e9bfdbe4-cd75-30a6-90ed-537d84b5020f | -16.6984 | -51.3576 | 2026-08-07 00:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 69bca1ff-ebc2-36ab-8e0d-443ffe69111c | -11.449 | -44.5587 | 2026-08-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 06527338-d873-309a-8bd8-20c6b3a580bf | -11.449 | -44.5587 | 2026-08-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 45de975f-15e8-3789-9521-150a4696fa1d | -11.4677 | -44.5791 | 2026-08-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 88efd2df-a79b-3281-97b7-ebe5ed213dea | -11.4681 | -44.5558 | 2026-08-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 29801cae-1fb5-32b3-896b-ce385c564074 | -11.449 | -44.5587 | 2026-08-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e0ba18ca-a4b3-3e41-a144-9ed2f9c8bc37 | -11.4677 | -44.5791 | 2026-08-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a6b53169-1991-3521-bebf-65cb659eb78a | -15.1169 | -53.5898 | 2026-08-07 01:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| f57c917b-b11a-3862-9ac4-a931a23e2847 | -11.4681 | -44.5558 | 2026-08-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 2cd5887b-b646-3f97-9673-7ad19348e416 | -17.7129 | -40.2695 | 2026-08-07 01:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| df143533-731b-3170-9dd7-ab4ec37d1092 | -11.449 | -44.5587 | 2026-08-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 60335135-6a1f-3832-aef6-fe1cf590e88f | -11.4681 | -44.5558 | 2026-08-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ad166329-958b-3f82-b47b-6d7da6cdbebc | -15.1169 | -53.5898 | 2026-08-07 01:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0d5351ad-f604-3238-95b9-ed5f87629c32 | -11.4681 | -44.5558 | 2026-08-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 25b93b64-0fe4-3d5d-8f45-52f6d87dc587 | -11.1443 | -44.4865 | 2026-08-07 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 515dafe8-79cb-36ac-be9e-9c47320a0470 | -11.4677 | -44.5791 | 2026-08-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| aea08428-3858-3656-8279-3731a6590bf6 | -18.16 | -47.977 | 2026-08-07 01:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5c688dd9-c6b8-3a5f-b5b7-64cb12fbfdc0 | -11.4681 | -44.5558 | 2026-08-07 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f89f8a2b-f540-3d57-aea0-0028528ae4b9 | -14.4353 | -45.6518 | 2026-08-07 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 17e33d02-e342-36ea-8e12-dfc1c20eae7c | -15.1169 | -53.5898 | 2026-08-07 01:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a446c30a-072d-3430-925c-3274f57c9f3b | -18.16 | -47.977 | 2026-08-07 01:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e7cffc31-0aca-3a18-ac94-da6436a121b7 | -11.449 | -44.5587 | 2026-08-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e8767f6e-0f7e-3d8d-b535-a5d8b6e43c81 | -15.1169 | -53.5898 | 2026-08-07 01:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 6cf8491e-ea7b-32be-8a29-7662ba43a0af | -11.4681 | -44.5558 | 2026-08-07 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0d876b63-2ffc-3a4b-999f-67b9854798e5 | -11.1443 | -44.4865 | 2026-08-07 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e0d289f4-f3c0-39fb-b94f-d6ca40beaa0a | -18.16 | -47.977 | 2026-08-07 01:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4560d714-05d6-35a2-84d7-2a2edc063431 | -11.1443 | -44.4865 | 2026-08-07 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 5b47f23e-36d5-3e8c-9f68-3ee7832ac2f6 | -11.4681 | -44.5558 | 2026-08-07 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9ef319aa-d907-3a83-bc4c-787788d34c30 | -15.1169 | -53.5898 | 2026-08-07 01:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8f7f7406-2337-3caf-bf38-9abf29c4bf04 | -11.4681 | -44.5558 | 2026-08-07 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 37c102b5-9f80-3b09-a786-637ae880cffe | -17.4855 | -53.3235 | 2026-08-07 02:10:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f5adc334-4ede-3166-8f60-0e0c3f93a933 | -6.4782 | -42.2397 | 2026-08-07 02:10:00 | GOES-19 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| ec3459e0-13b9-34f4-88ad-7e0c82de7faa | -11.4681 | -44.5558 | 2026-08-07 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 8ce7ded3-cd38-3831-96d2-d21cb787a344 | -9.6254 | -40.5875 | 2026-08-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 2cb8d435-3548-305e-bcc1-b0d2847610d5 | -16.5171 | -49.6996 | 2026-08-07 02:20:00 | GOES-19 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f6ce0b82-f89b-33ee-820a-6da54e874d79 | -16.5171 | -49.6996 | 2026-08-07 02:30:00 | GOES-19 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6d80971d-3f40-31a3-abd9-41bba5b4d08d | -11.1443 | -44.4865 | 2026-08-07 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c6fb03b4-1977-33e7-8e1b-a612257cd239 | -16.5368 | -49.6962 | 2026-08-07 02:30:00 | GOES-19 | SANTA BÁRBARA DE GOIÁS | GOIÁS | Brasil | 5219100 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |


[Clique aqui para ver as próximas entradas](README6.md)
