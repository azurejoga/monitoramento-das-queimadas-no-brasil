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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a34ff4-b142-31e2-967f-6eb394776066 | 0.51123 | -50.779 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13bd427f-561c-39d4-810d-54ec7694e538 | 0.50786 | -50.78344 | 2025-10-04 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d3badbe-e2e8-3905-9a99-1f4f78d6d3c5 | -6.80996 | -44.62164 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fe2c83e-f2e4-36db-91d6-95a7d5ac785e | -6.21983 | -44.2766 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a321ada-6074-31a5-b0b2-3682205ebb02 | -6.27161 | -42.44888 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ce88e324-0601-3793-be7b-6f0282d47ef3 | -4.26366 | -48.5505 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a1bb54-7365-3d73-85c8-d7e6e53d2116 | -5.60815 | -45.19902 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a14ae7c7-a195-3edc-8d91-9c74628d8dd1 | -6.82092 | -44.68308 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 571c2777-ea6e-3a6c-abc6-afa6f4aacf8c | -5.87291 | -44.27723 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51aec0f-f9b8-3dae-965a-6fa0633eb1a9 | -5.19806 | -45.06837 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| fb574e78-9c3c-3d2f-9e4c-c7052e037760 | -4.61426 | -46.46013 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af49f5fa-b270-3eca-bb0e-6a3e5ea06495 | -4.43429 | -43.24245 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f6b8e7b-b68b-324c-b7ff-7886ffbfc087 | -7.16056 | -49.30483 | 2025-10-04 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 225cc556-0810-3410-8587-955f27e00da5 | -5.9015 | -42.53597 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| badf223e-abfb-36db-ae57-8cbfe755e067 | -6.35761 | -41.6197 | 2025-10-04 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca046161-5966-3f9b-aacc-d38e2539c07f | -6.35938 | -41.61977 | 2025-10-04 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae0196ac-77a8-30a4-9eea-3bb92645aa6a | -6.66512 | -42.81951 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1840a026-50a0-3a01-a84e-11815c8b827f | -6.60317 | -44.2978 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de9ecc4b-021f-3203-a291-903569094ca9 | -6.45091 | -43.445 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0fab32e-ef6f-3147-96f0-bbc3a047e946 | -7.70837 | -42.57782 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38ea0b3c-cd63-3083-b648-a55b842afbeb | -5.84609 | -42.79996 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f380d2ad-47d4-3c88-bfac-1ee36595c087 | -5.97973 | -43.6091 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17ed7fe2-85c8-304f-bec4-b57db27d24f8 | -6.46403 | -42.52131 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 88969383-b7ad-39c9-a1f2-70311a10aaa9 | -6.99051 | -42.32589 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6301408-7be8-3a78-aced-43bdb3d2acc8 | -6.34263 | -43.44172 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42af3a3b-6abd-37d9-b6bb-41db4e4296df | -7.80536 | -42.52122 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8210c6f7-167c-3e9e-9ea2-2cdaa5748d4e | -5.47408 | -42.76926 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 77aae2c6-de47-3f68-901f-8f50af44176d | -6.54639 | -43.87124 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7fa9e0e2-a56d-37b7-8f56-d94281561775 | -6.19993 | -44.3362 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 815419bb-cae4-3228-a43d-8364adb372de | -5.95443 | -43.49046 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c06f6f02-32d5-332f-acd7-7a51ec7d6f6c | -7.23702 | -42.98458 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6201c17a-2dcd-32d3-862a-0b9ba2f37a4e | -3.84312 | -41.58494 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c00e7e6b-02c9-363f-8e3c-8dae4a330fb9 | -5.97257 | -45.27209 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52e2a5bc-7418-3d61-86dc-fa8e94a25ee2 | -7.64435 | -45.47032 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a46ab6c-0c87-35b2-9c76-78665edee0e4 | -6.34374 | -43.4561 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a210d2c5-3cb7-31e6-bb34-9ec688f37d25 | -5.68843 | -42.83167 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d947f8d2-137e-3828-aa2c-cb1507ca6e0d | -6.34208 | -43.44518 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5b52829-161d-35c0-a016-6569f6b45d30 | -7.01453 | -44.85334 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32fee4ad-accd-373f-956f-662f2d57e266 | -5.31852 | -43.53621 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca0618df-c5d3-3195-8f6a-e502132b5b32 | -6.66659 | -46.15236 | 2025-10-04 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c94dbbb-bfc7-3d52-b634-0287b679e581 | -4.66581 | -41.51161 | 2025-10-04 04:12:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2347dd88-6226-391e-82e9-bb7576907d71 | -7.75002 | -42.54845 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 707116ec-e96d-31e2-b3f9-a4bbe7196973 | -6.66567 | -42.81605 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 530164e6-2aad-33c9-9150-0d079da2113e | -5.08083 | -44.09378 | 2025-10-04 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 81dd4efd-c3cf-3faa-8825-0d4942f7510f | -6.26136 | -42.79472 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 97e859bc-fc1c-38fb-aabe-f83c8c26cc53 | -5.937 | -42.89186 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a6b1ded8-11ce-385e-91a6-da3f727eefe1 | -5.82257 | -42.88466 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1657bdc8-8725-3f39-84d5-099a2d871ad3 | -6.07852 | -42.51053 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 730d08bb-a42b-3233-a425-8c8fe874e178 | -6.37154 | -43.90095 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba0dfa9a-0503-34f8-9d17-0d3c01d33231 | -7.56092 | -42.62952 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9873d930-8930-3ca9-abb4-f704bd157669 | -6.60144 | -44.30853 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b16b4d4f-c331-39dc-9821-5bea5bfb381b | -6.07388 | -44.6181 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fa0cbac-701a-38fe-b100-3b7829082d6c | -6.03723 | -44.58598 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff1c2dc9-3912-36e0-aaeb-6a2254724020 | -5.26048 | -39.26513 | 2025-10-04 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d91ff3c-0d6e-3496-804a-14bdb49123d3 | -4.64355 | -43.18677 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0d52871-b823-381b-9bd4-ec68bc8e9b80 | -5.83834 | -42.8728 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9046e9c8-9b00-3ff2-a550-ef778a2454c7 | -7.73413 | -42.60689 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2e4b8e99-70bb-3022-b11b-547d7248852b | -6.78931 | -44.85836 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad6ba9d1-f6d0-3931-8430-c8a29bed392f | -7.46711 | -46.84758 | 2025-10-04 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c965f46-01b5-3155-97ce-47a48bd14f34 | -5.2545 | -42.63248 | 2025-10-04 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10bad980-b0cf-35bb-9eab-83f346af2a60 | -6.34705 | -43.45662 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d3b4020-9fcb-3af6-8a02-288fca91c592 | -6.37333 | -40.79955 | 2025-10-04 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b88ee19-3497-306a-8307-9ead907af5b9 | -5.4671 | -43.15726 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ab3e24c-1420-31e7-b8aa-3dc63430f7e0 | -6.17153 | -43.92019 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0bb33ad-2033-3890-ab66-c3ba76437c51 | -5.87315 | -45.82138 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df80c1ae-1c47-3544-a74d-9dda7179cac3 | -6.29203 | -42.44855 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 083090bc-0185-3b2a-8115-0dbc570ac986 | -5.67507 | -44.19801 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ef0319-f351-3f52-91fe-e52002dd5cfc | -5.80243 | -42.73297 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9dc61129-211f-31a1-b2f3-fcf9dbcd1d71 | -5.45218 | -43.16552 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 013b4966-deab-39cd-ac4a-12d966ba2101 | -4.44868 | -43.23759 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4952e25b-c59f-39f5-8daa-8da1d55941eb | -5.86813 | -43.56245 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08dc194e-666a-3123-8946-323c13c65be0 | -5.24591 | -45.55565 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 704e67b1-9315-343e-ba8b-ee7b81eccabc | -6.65461 | -42.80013 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 824b199f-b4d1-3c91-b894-34ff3303124b | -7.72053 | -42.56537 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3bd08fa6-0bda-3518-b50d-afa6194b911e | -6.30801 | -44.27632 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86c7d6a5-31ff-3e5f-a847-34592cf646b9 | -5.473 | -42.77616 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b4f5d1c8-0ee2-384a-844c-97d0405ff1f2 | -7.70118 | -42.58027 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8603837-bbc1-372d-a9e9-472774f23578 | -6.37543 | -43.89797 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e92d6142-d906-375f-a009-14ce76b5b15e | -6.28412 | -44.04593 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a3acdb-95c4-3eaa-9b57-0188847b4fd8 | -6.65742 | -42.82537 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cdac4aa8-7589-3ea9-a014-8960e7b78c3b | -2.68217 | -48.39607 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b912b8e2-260c-3785-b7a6-4d5a3acb6e2a | -6.29876 | -42.49221 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7704b55-8b7b-3910-91d0-8d3942ab5f46 | -2.29761 | -47.99435 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c57a23e-c51f-3a36-bfc0-3ddb17e92055 | -5.59075 | -44.19603 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4dcefa3-3b13-3ff9-97da-457414c862f9 | -3.68267 | -49.05544 | 2025-10-04 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7629d5e8-f9bd-3252-b1fe-8335b2afd475 | -5.82642 | -42.88173 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cfa72abf-d1de-351c-b029-8e3b97c59b27 | -4.66527 | -41.51512 | 2025-10-04 04:12:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae7fc395-c341-3f04-b991-7bdf41d72f29 | -6.66182 | -42.81898 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20311338-fbcc-38ff-921a-65251a951de8 | -5.30409 | -43.11345 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98095ef6-d611-3cee-95e6-b5bc13381c6e | -6.24051 | -45.34409 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9d21b7d-f536-3e46-86bf-a4135546835b | -5.63608 | -43.18436 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e9d199e-238b-3a09-8229-74a1a783043a | -6.24685 | -45.34902 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a0ac2bd5-e494-3fc1-87ba-c841e4cb6c4f | -5.66724 | -42.70813 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da70a221-2410-35e1-9096-623616bf5792 | -6.28264 | -42.4435 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d10117ba-e229-3a8c-8f9c-35c913203ab0 | -6.35934 | -42.88486 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb7dd456-238d-3fcc-96ae-382db22cfb3e | -5.62907 | -44.70262 | 2025-10-04 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 552d43c3-404e-3fd0-923d-6e1de530fadf | -5.7637 | -42.93552 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c505aedc-e617-36b8-bee6-70edf02d88ba | -7.55314 | -42.39521 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 495df513-4a19-3b99-b635-2f1430d384ee | -5.69672 | -42.84358 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0630df33-047c-3eea-8754-6449c6152c1c | -7.24698 | -45.32613 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
