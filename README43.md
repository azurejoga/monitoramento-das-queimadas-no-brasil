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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 750f1b3f-4486-365a-b471-7fbaf5a7af1a | -14.8683 | -51.84724 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 82ffd4c6-a15e-388e-af30-521af8929e63 | -12.77279 | -54.00987 | 2026-10-01 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9e300c0-06b9-34ef-b1de-14c3a637028d | -19.03949 | -45.66581 | 2026-10-01 04:17:00 | NPP-375D | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a09cf477-5ded-30c2-b6e7-5b2a8b375cd6 | -13.3188 | -43.82331 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a9e8220-76e5-3437-8105-fa59b7c4e53f | -14.14591 | -46.24125 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae07576f-0644-395f-a1fe-567fad223d4d | -16.22276 | -43.62051 | 2026-10-01 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3657a437-a29f-3e23-b780-06c5c649bacd | -15.12141 | -43.62118 | 2026-10-01 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b476e226-fb9f-38a9-9a2e-d308840aaf2b | -13.5157 | -46.88591 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1abc16b2-aa08-31f9-aa42-6b37662eb3ea | -14.87076 | -51.86341 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e60a2b11-7fbe-3c40-b8c5-eec02c836cfd | -19.7175 | -43.24557 | 2026-10-01 04:17:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ea2535b-e7d2-3e84-bbaf-bec21ff14dcd | -14.14755 | -46.23457 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be20ae42-4ab3-31ec-8db9-e16aa35c274c | -18.44762 | -43.67017 | 2026-10-01 04:17:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c094d047-4669-384a-ae9a-c36a7b23c158 | -18.51158 | -45.1443 | 2026-10-01 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27b9e668-0694-3aee-944d-aff92e5d5293 | -15.22956 | -46.15109 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3556a690-80c5-312e-916d-b8b55574a2d7 | -14.14202 | -51.13507 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94a3ed1d-c3dd-333d-b07c-10755b5b3287 | -10.77109 | -54.75346 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a6b8d82-55b8-392b-9d1a-fd8c6db26c05 | -16.35606 | -42.58447 | 2026-10-01 04:17:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7b84933-d581-363f-b17a-0c856dc3a2fa | -15.60681 | -38.98431 | 2026-10-01 04:17:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1c1610dc-ad30-3d12-b6d4-01b034ddd4ef | -19.59863 | -43.91659 | 2026-10-01 04:17:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69356ef9-99a0-375c-ad01-8f751c46bb83 | -15.60321 | -38.98376 | 2026-10-01 04:17:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0883b239-a126-3414-b362-5a02efab3ec2 | -12.77849 | -47.26786 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d234fc4-cacf-3a16-b222-9d3939975544 | -14.40297 | -51.25692 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a64be022-bf3f-3e0a-ad77-1a4cc9ff92a7 | -14.87551 | -51.86835 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6340e30-72fb-3919-85f1-463be2e6701d | -14.26938 | -44.50255 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4989365f-d5c0-39cb-bd21-cff9e013d8db | -14.41506 | -51.25229 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bee3828-0b3f-34cd-8c6f-308ebefb08e7 | -13.38414 | -46.81255 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b680b04c-8186-37a4-b281-02d4a680405f | -13.68074 | -44.29002 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1164029d-7dd7-3090-a0a7-4093a0a32008 | -13.6545 | -53.93375 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4ef5336b-0223-3722-97d3-016fd2f7b254 | -14.48537 | -48.30812 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a2ee6d92-cf83-3a4f-9e16-8e69664757f9 | -15.77655 | -46.03284 | 2026-10-01 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7978a304-a703-3b67-80cd-600d0016658d | -13.64693 | -53.93789 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| acfeba8f-c2d2-355d-a0fa-07f36c065849 | -15.2692 | -40.61576 | 2026-10-01 04:17:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a753eab-f6e2-3853-bfc8-445e8066210d | -14.37108 | -44.75866 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f5d8fc0-ae38-3dec-954e-fc8c9cee28e0 | -12.58127 | -47.16219 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41e6410f-9656-3f85-b22c-0119534e39aa | -18.10766 | -44.41423 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d45c0aeb-4739-3d5e-8ea0-ebac8ad1a5d1 | -17.21568 | -46.84327 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25486304-e671-317f-837d-2f7ef91e2c00 | -15.23428 | -46.1466 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e9efba5-c33e-3f71-afd0-9460fc1047ed | -12.85526 | -44.33805 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82fee410-169f-365e-8686-f453cbdcb521 | -13.38353 | -46.81598 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea4afeb9-3c86-341b-9783-139bf742cf61 | -13.55084 | -43.51899 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc41d3dd-80c6-3204-85d9-10c5b032d4b0 | -16.17944 | -42.88203 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 222150df-24f5-3bfa-84fe-c98888616142 | -13.43733 | -42.49276 | 2026-10-01 04:17:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b27e6942-1f22-30cf-8535-7e7e4b2ce6fb | -13.38091 | -43.99208 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80f97a58-7812-33c5-bcff-cef2407243cd | -15.1627 | -46.12823 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83b69424-ab0f-3531-a5ee-d98960890d16 | -13.38977 | -46.82848 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fd4bc40-5bea-32b4-8a8f-ce322381ddf8 | -13.73543 | -48.97578 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf0d2548-2ac7-3038-a23a-f98ec0035caf | -12.85598 | -44.3339 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c468e01b-45d6-3232-a995-7bcbd7528d2a | -14.40901 | -51.25461 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecd2677f-35b0-369f-844a-4eea65682ed8 | -15.40188 | -42.80941 | 2026-10-01 04:17:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8e3bf6-8d33-39a6-8d94-715a89552617 | -14.43902 | -51.27186 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb639269-540a-346c-a68f-c69a0c763aef | -13.3675 | -46.83485 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40af8d06-787a-378a-a123-ca752a8e1f27 | -14.41436 | -51.25576 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07f1041d-a432-30ba-a14c-ced4a2088e13 | -14.38788 | -51.29366 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9f61bc47-7520-3b7c-9ebc-526c26796c8a | -14.38184 | -51.29596 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e73e7cc7-2aaf-3d4a-bc18-dd6ebcf210b8 | -14.15201 | -51.1408 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2b2e290-1d31-3d30-9ef3-5b4b2ddc352b | -17.91635 | -45.03067 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09a08e21-6a5b-36d6-8606-e40396bead74 | -13.37969 | -44.02068 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4cab7c1-e3f9-3478-a11c-02fd933da99d | -13.38211 | -46.83737 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b91278fa-a8bd-37f3-b18c-ccb402e8b27a | -13.07017 | -51.18438 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31cea637-19f3-34ec-b828-c80b929017a6 | -15.92016 | -43.52589 | 2026-10-01 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdb19c18-d89c-330d-a3f3-eb0a5f78d6a3 | -11.73662 | -50.40891 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85da14ad-718e-365f-9825-0defdefdbe97 | -11.73363 | -50.40825 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d105f5a-8760-3a23-9e26-24effec149d4 | -18.0653 | -44.5192 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 601b5991-378b-3617-922b-d4b9868aef35 | -11.83631 | -50.50623 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c44432a6-7b48-320c-b367-4dd86081d7b3 | -17.91078 | -45.04224 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2df26ca3-44e2-3582-bd63-491fff50a5a1 | -16.13558 | -43.74377 | 2026-10-01 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 260daa5b-f118-3317-ab0f-56cb5bb3da5d | -12.18241 | -47.38705 | 2026-10-01 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bac6ec3-d9e6-38a8-bfeb-c5ae4a686f3e | -14.55355 | -42.74036 | 2026-10-01 04:17:00 | NPP-375D | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a5cd40f-1041-3552-85c7-e378d9bec7a2 | -16.67544 | -41.84955 | 2026-10-01 04:17:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 83ea14de-6cc7-3e9a-b522-9ed6092a0aa8 | -13.25981 | -42.46375 | 2026-10-01 04:17:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a76bb9ce-a4f3-3d2b-9342-95ad96453f85 | -17.08219 | -46.82278 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c265ca71-603a-3c91-880c-821ded064bf5 | -18.06742 | -44.52759 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0e8cf563-b7fc-396f-95a2-46d7ed4a1f6d | -17.87952 | -44.31342 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f9c19b1-05d8-3f95-ac1b-de60ea8e3404 | -19.34452 | -41.45084 | 2026-10-01 04:17:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 455a681b-ee33-320c-a481-8273d77e5461 | -14.39762 | -51.25576 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 3f25bf1e-1c03-3ffd-86b2-a90e9a45ac96 | -14.87304 | -51.85222 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5d5e903-1849-3502-8c97-64e0d9cb7aaa | -13.6709 | -44.30502 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fe94201-aa3f-307e-94af-059c5b935f12 | -13.88429 | -44.45437 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d994f34-d131-38d8-a875-ecba100bcb48 | -15.2325 | -46.15681 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 937078e3-6f32-34a7-a143-3287d53abc10 | -15.64072 | -40.9878 | 2026-10-01 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 43cc2bcd-6243-36fe-9763-8d4a82d18033 | -12.18826 | -48.44442 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b21a285e-d6ba-329e-8b89-153f252010a5 | -13.38173 | -44.00861 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffbbfcd2-b38c-376d-9078-0d2eb621d7bb | -17.91286 | -45.02998 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f77e9608-71aa-399a-8799-e9ccd28f2267 | -14.74036 | -45.19951 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7efdbee4-bcc4-3520-9869-8072fe4e6c17 | -13.38509 | -46.83104 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 130586cc-038a-395c-a8f3-7d6281f52460 | -17.88293 | -44.31403 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d2d6be3-8234-3916-871b-b169eb1e3937 | -13.10892 | -51.21895 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 179b38f9-ea85-355d-8416-138b32d4f364 | -13.66609 | -53.9421 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0fe98742-d12a-338b-b9e6-5d1b9762faf1 | -12.19008 | -48.43454 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 09c8bb41-d649-30b2-b0c2-59f6e52c5927 | -15.96856 | -52.48279 | 2026-10-01 04:17:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 096887cd-a1cc-3788-ae9f-44910a747f2d | -14.86753 | -51.851 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 55fee1d8-bc4b-31a4-a76f-137c7947a3ad | -14.13875 | -51.12366 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 692e95d8-bd68-3c76-b888-567bfe63063e | -15.23132 | -46.14097 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcaadd8a-8614-3982-b2c6-2630550db1f8 | -13.53842 | -49.189 | 2026-10-01 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d975d973-1792-3f00-944f-a987b405fe8f | -14.42645 | -51.25112 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c79c725b-e450-3d87-a79c-72877c766375 | -12.08793 | -50.69441 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80620cda-a1f1-31b9-bb89-91c6b99d7adf | -14.23714 | -44.22673 | 2026-10-01 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67d8c0de-0943-363c-a4c7-55abd40d3dc8 | -14.37467 | -44.78108 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 186fb785-1ed2-3292-b2b1-f6a43f52107f | -15.2381 | -46.14724 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 872c8551-cde6-341e-b81d-254f24a26c39 | -13.38592 | -44.00523 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
