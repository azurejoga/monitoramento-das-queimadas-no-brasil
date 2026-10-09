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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beb690e1-d1c6-32a1-9393-0277be31adf8 | -1.0945 | -54.170601 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f465550c-e91d-31e3-947b-ef96b585fbf5 | -9.294 | -47.4366 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab5ecc6f-a7c2-33a7-8888-a1ae398a2294 | -6.0114 | -40.962502 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f7960635-c8ff-3ee9-ab01-92957175bab9 | -5.6734 | -46.357601 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4407fe48-cbfd-3274-aa8c-01a9f5e530da | -5.353 | -45.724701 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8a59b04-9478-3438-9c65-616e3be42c2a | -11.6375 | -43.715 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5b6d155-7bd0-347f-843a-b311e656521e | -12.0159 | -43.4767 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 937de9bc-bac3-3e13-a691-9220e11ab312 | -4.9887 | -45.307499 | 2026-10-09 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81b264d2-13b6-3452-82e9-f33c71a9bd53 | -8.2211 | -46.4128 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3002d432-174a-3645-8e03-98ff3e128cd1 | -6.1219 | -44.808701 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d15d030-7a2d-3021-9824-b1b6f7bb82ba | -5.3519 | -43.406898 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7689f831-4a70-39c8-ad9b-8915a5d153cd | -3.0035 | -54.066002 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ffffc54-77e1-3ca7-b3ca-d723853efb55 | -5.9558 | -55.371799 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5440a65b-7fa2-314f-997d-0b2758bd243a | -3.6974 | -47.680199 | 2026-10-09 00:28:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d323af-52bb-3c14-a6da-93673bd530e9 | -6.9303 | -43.668999 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4a0d05-ae6d-3f14-92fb-a70c20eff1e3 | -4.0469 | -46.909199 | 2026-10-09 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb812866-4b2e-37b7-a1fe-b9be1ae5f4ee | -5.7026 | -41.743301 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9156a76e-721c-3393-a717-3b38e33d1895 | -9.6138 | -40.617802 | 2026-10-09 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cac096a8-2343-3534-8670-5e8e0893b30c | -11.7825 | -45.581402 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d014b43b-0d08-3e8c-b2b5-137aecde28e4 | -6.8863 | -45.890301 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4feaa7b7-e850-3f9b-ac2b-9af05219184d | -7.8966 | -54.732899 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218f71e5-0eb2-3367-9bbb-72eb6dde5563 | -18.0849 | -42.263 | 2026-10-09 00:28:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3ed90e5-c11a-3ef8-a890-f35ba1231454 | -9.6017 | -40.610401 | 2026-10-09 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1083ff34-4345-35df-a931-191cfe8a9434 | -5.6213 | -44.385201 | 2026-10-09 00:28:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aceb9208-7f46-3d4c-b8db-1b85798436d7 | -6.1235 | -44.815701 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7f66c6-795a-38bb-9613-7c1673510c63 | -12.4709 | -41.321899 | 2026-10-09 00:28:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b4978f47-4565-33a4-b5ec-7a4cd1c84311 | -2.3272 | -48.494801 | 2026-10-09 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e6bdf7-9b37-35cd-a831-9d2f08e5f257 | -5.7015 | -53.487 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1846901f-344c-385c-a98f-5de5105445c0 | -3.247 | -50.411999 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76ed50e-3b53-3abf-a469-b3eb11260c6d | -5.8804 | -43.416302 | 2026-10-09 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6865a8-bd43-327e-bfec-b446de1bd144 | -5.0937 | -42.6586 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5bca2997-bd82-3048-8877-cff673f6e3d5 | -8.9774 | -47.538502 | 2026-10-09 00:28:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0a80c23-52fc-3411-a1b4-ee6432d5a627 | -5.3893 | -44.186001 | 2026-10-09 00:28:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77f824c3-a4f2-3e96-8b68-e3d718b6e174 | -2.9944 | -54.116501 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71f7b299-1817-3228-8356-7f6838dd0e12 | -8.3286 | -45.028599 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 098aa5a6-aaea-3c44-a190-1a84873dc6a1 | -11.3048 | -46.673901 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca339680-a759-35d0-bfc4-506dbc9448e1 | -3.034 | -54.156799 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 786d07eb-a5db-360f-980a-8a8aa19722ae | -2.9909 | -54.101002 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b947701-590b-34f5-9a51-393508a53bcd | -13.1391 | -54.331001 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8b64f20-e3ee-3da9-9195-e7dece5e1833 | -18.639999 | -41.352001 | 2026-10-09 00:28:00 | METOP-C | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b726699f-2960-3776-8f20-64a501c09f85 | -9.6236 | -48.892502 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4ade719-abfa-3e7e-b0ac-75d3c7d827ea | 3.5556 | -51.280399 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b5e528b0-2d94-3170-9e8c-162cdcbd62af | -8.3193 | -49.1185 | 2026-10-09 00:28:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5dded3-cc77-3976-b078-6e3dd52b9802 | -4.0835 | -44.1171 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 961d3c4e-fad1-3c8a-aa3f-4ba00c883d3e | -11.6619 | -43.686798 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| defbd9fa-8e90-3fcc-8079-128f22eaa6b9 | -9.798 | -44.780102 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b229ec9b-29e1-33a6-ab63-57fc72eccc3e | -1.1043 | -54.168499 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21a2fb87-eb3c-3565-8e7d-4a838bb51db1 | -4.2649 | -46.285599 | 2026-10-09 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64d45af0-be58-3b6b-bbd8-198156b10cd2 | -8.3212 | -49.127399 | 2026-10-09 00:28:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e363d68-aacc-3350-a7ad-1b2df6dc2416 | -10.1559 | -44.676201 | 2026-10-09 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b25b2f3b-ae1d-342c-82cb-5a83cb8a40ee | -6.2517 | -45.326599 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8b9c2b4-b5a9-3dbc-9b88-7b01cfa91da5 | -16.5865 | -46.765099 | 2026-10-09 00:28:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d2f25dad-1260-3c1e-aca9-e9cf2648e741 | -5.1055 | -42.664799 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64f75c8e-fbbf-3e50-b554-2141ab4dfa83 | -15.4298 | -43.245499 | 2026-10-09 00:28:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1972cdd8-31f8-338a-b654-b3ee9955077b | -5.2398 | -43.987 | 2026-10-09 00:28:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9821e55b-e68e-314a-b6c6-60097bc87106 | -6.76 | -45.788898 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9f973b3-0f25-31e2-9897-d2074c6484ee | -2.7336 | -54.092602 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25abe7ed-98bd-3c16-b295-43f7649ef97f | -2.9621 | -48.748299 | 2026-10-09 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b7c964-c1de-3275-a13d-f169d4e3bd88 | -8.2015 | -46.417198 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2fb34c2-6a5b-3207-9783-55100fff8cc3 | -0.9923 | -47.663399 | 2026-10-09 00:28:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea197955-1b90-3c68-b97c-0bc4aa072d40 | -11.411 | -46.689602 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92335249-852a-324d-9d07-73e774dca89b | -14.3928 | -43.810799 | 2026-10-09 00:28:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24ac27f1-a5a5-3730-b773-acbcf669988a | -4.6238 | -49.2225 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a28db0d-ba7b-3c88-bba5-90d6dab36a24 | -9.4468 | -45.865101 | 2026-10-09 00:28:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc8b9a7-b8f1-35f9-95de-ab9d25079159 | -7.2161 | -55.155602 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fecf6eb-66d4-3d22-b691-0e74bbb8d905 | -13.1585 | -54.327301 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9001bed-0139-3669-ae4a-00822887b8af | -7.6941 | -45.455002 | 2026-10-09 00:28:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39fa2c77-e24f-30b9-a60f-51f0b9602221 | -6.4932 | -55.3269 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc2bb07b-8b16-3b54-9c4a-02a5887a6d66 | -7.2124 | -55.089802 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6622f0c-6d9d-36be-94da-91682e23f615 | -16.8859 | -40.7075 | 2026-10-09 00:28:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3ae29d1-2f75-3a9e-b0a0-98b88e9a3ed5 | -5.746 | -43.283001 | 2026-10-09 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0abbaacf-121f-35b7-b980-0cc80f67aad6 | -5.9224 | -51.833099 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f349ea9c-a95e-37d2-83f6-664a281d45eb | -12.0061 | -43.479 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7577d866-b670-3f1a-adbd-ae7427db2af5 | -11.0706 | -44.076599 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7796181b-8e3e-3946-9c0c-b7210885a05e | -6.5039 | -44.364498 | 2026-10-09 00:28:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b742cd42-4332-3ddf-8377-1d1400d49174 | -11.7659 | -44.9571 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac310885-7a10-3f32-85c6-d5354d5383a0 | -17.2344 | -39.530602 | 2026-10-09 00:28:00 | METOP-C | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f06cdc7-2ba3-358e-a83a-851275dd4b89 | -6.0164 | -40.9832 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1226e36f-5e8c-3dd9-b435-db73a8fd1bb7 | -11.644 | -43.698502 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25408169-fee8-3c31-bd0a-c0a29a034710 | -11.23 | -45.3218 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 506d7fbf-2347-30ec-88c0-f5f3b68d5815 | -2.7342 | -54.140701 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b87ec07-dbbb-32c5-85a9-b10e3e17da7f | -13.1672 | -54.373798 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 480a7e81-2228-323b-892b-77f068d3ae75 | -4.7237 | -55.674801 | 2026-10-09 00:28:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec900e9-81e1-3f01-bdbe-14b6ed7e2e5f | -4.7334 | -55.672699 | 2026-10-09 00:28:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc1a7de-5de7-3e6e-a549-37e14b2aed50 | -11.4129 | -47.590698 | 2026-10-09 00:28:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbc20680-f565-3686-9409-a12f42c99c5d | -11.0754 | -44.097599 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09af154c-3b20-3015-9a2f-351aa46c6929 | -3.0076 | -54.130001 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd536cf4-2b5a-39e7-bda1-5e0ee634489d | -11.4574 | -43.382099 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2d1e30a-7f22-33c7-abbf-178be273fcd2 | -5.8543 | -47.424198 | 2026-10-09 00:28:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01d48216-a65e-31b5-b11f-8635d9723f18 | -18.7887 | -46.484299 | 2026-10-09 00:28:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b8afcf0e-6440-3d6e-9a7d-1b237409f40c | -15.2577 | -42.360401 | 2026-10-09 00:28:00 | METOP-C | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ecb4ca66-09b4-3abd-9776-63531674e9e7 | -7.473 | -42.857201 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f846e10d-66d1-3a67-bb72-b1a0805425f4 | -8.8967 | -44.9426 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2ccaabe-db0d-3a3a-9040-dc61b3d5e3fc | -5.957 | -46.3806 | 2026-10-09 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1520718-4853-3093-af05-4875b46885ed | -14.9601 | -47.5522 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af63ab6c-3cd6-3bdf-a532-6cc8e6625df2 | -11.7872 | -45.602699 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6bdab460-658a-3687-9e94-48432cec43f0 | -6.1445 | -47.9342 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2211cdf7-29f1-31c1-b478-8642ec2526be | -4.622 | -49.214401 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf615325-edad-39d3-a512-afdc4eb4f539 | -5.3024 | -45.728901 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90b11370-bf29-37fa-8f19-cc595032ecbb | -13.4063 | -39.799702 | 2026-10-09 00:28:00 | METOP-C | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README27.md)
