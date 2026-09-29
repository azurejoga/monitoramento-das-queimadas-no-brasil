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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84212280-a319-3b11-a404-0a4173994c19 | -7.5156 | -55.03998 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac579a1-232a-3246-aeba-e3a0eb87f701 | -12.31455 | -50.29568 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abc2c6ec-49f8-30e3-9c7f-330414598fe6 | -11.37271 | -54.04654 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aaf0956-419f-3914-897c-346729eff0e5 | -11.41884 | -43.43779 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eba19d23-c2e3-3c18-bd3c-14f9ff176115 | -12.01454 | -50.93246 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2cd2372-2348-3434-8add-c2b98907b885 | -11.42743 | -43.46648 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b14547d-d488-3571-9f37-1e9a9cf7c250 | -11.39296 | -43.45564 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f135c6e9-3d54-3a02-a94f-fa4d5739e7ac | -11.8679 | -47.08742 | 2026-09-29 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0133acc-d549-3144-a927-999a67d224ed | -11.39687 | -47.45286 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feb1082e-45a9-3ceb-982a-c410042a5f4a | -12.03526 | -50.94412 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60e6d429-f96d-35e8-badc-d031e326eead | -11.8988 | -50.62288 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d20f4c5f-de45-3048-aaf2-d16a00fa4ada | -12.01337 | -50.94106 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 923356e8-a890-306f-98c3-651e242a2a0b | -11.39765 | -43.43559 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80c2a38e-91e8-3a80-ac99-2bd6ce50121f | -11.36851 | -54.05014 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d3ea2bd-731e-3b86-8523-bbf30919cdf6 | -12.94395 | -46.66789 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96052634-9cfd-37d3-96d1-2adab18ba665 | -11.42887 | -43.4738 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e6fdfbad-b8c5-3a09-bcfd-dbb26eaec119 | -12.69735 | -47.26069 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dd70c6f-1288-3de5-be8b-c1386ddf0141 | -8.742 | -47.87631 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 005258bb-166a-30b4-8131-69e79ff7984a | -8.29238 | -54.70763 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90c37529-3192-35e1-a15c-5d229b75f889 | -12.00841 | -50.94474 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ad1f81b-888f-354c-8b9f-c36b0c5fbcfa | -11.35651 | -54.0568 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f344919-b16c-3248-a214-288cc9d1a77a | -12.61206 | -47.27832 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a255fa5-d21c-304f-a532-d71d1ddbd785 | -13.55817 | -48.94175 | 2026-09-29 05:12:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9655834d-6976-3687-8036-ca45f19761b4 | -13.52478 | -46.90026 | 2026-09-29 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01fe459a-4ec5-3b28-8c15-c1c67d02b10d | -7.49883 | -55.03737 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c45a63-efd0-3697-a55b-aa615140ff44 | -12.72352 | -46.99286 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 43f69277-f5fd-36c9-bdcf-1861d234526d | -10.42276 | -53.83048 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b37655f0-d046-3dab-b23e-5c2ed7e425c0 | -13.43173 | -48.62316 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 054407ad-771e-3a10-81d9-b152163a7af6 | -9.17057 | -61.40275 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ecbc2912-88ec-3bd6-91ba-5980f03610a7 | -13.17873 | -48.55666 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0427edd0-8b5b-3dbd-8ad4-5815a102e488 | -11.30567 | -58.33877 | 2026-09-29 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38376e15-e4dd-3f06-98a5-a6ae8d02a447 | -7.51224 | -55.03946 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af5f5cf-2d90-3bc6-860f-d39891922327 | -9.79482 | -48.20161 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c8b494e-7f4e-3b79-9ef4-5ed63d18c241 | -7.55859 | -55.02851 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dbd0e44-36bf-32ff-9eb1-6cefb3ebf412 | -11.35117 | -54.04327 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9702c251-57f0-35c0-9e13-dbe837945549 | -11.18657 | -44.8271 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26f3b3ac-0a65-3516-8c89-62e9a2054fd2 | -8.28219 | -54.70604 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0886c9a2-c826-37db-a5ac-6cb43e5293d1 | -9.01338 | -61.03124 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8723144-6313-3f52-a07b-c50f0517bd97 | -10.39018 | -61.24517 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5b8c398f-0182-3aa5-a984-14776ae3b5b1 | -12.04579 | -50.93245 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e47687e-7ca5-3303-8194-a4287925c296 | -11.00736 | -54.14729 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06c6d37-5ac9-3002-9754-f95aa1f8dad6 | -10.39318 | -61.25065 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0d6b34a3-1598-3f3c-9cc9-2452066ec353 | -12.16008 | -50.81857 | 2026-09-29 05:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81af4136-3749-30a1-a407-88608d752a5e | -7.51895 | -55.0405 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a2c10d-8a75-3dc2-86c6-cacf3a54532c | -8.29805 | -54.71608 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 191e2167-1144-3529-bccc-2d6df40a285e | -12.72268 | -46.99995 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9d049eee-bfa6-36c5-ac31-20d2b9ea76a0 | -11.17811 | -44.78714 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1769c0e1-84c2-32f1-8425-d03ace50589d | -11.37568 | -54.05126 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c52e51bc-7980-30ee-a986-2a5bfb420a9b | -12.01573 | -50.98935 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37ff37cf-5278-388b-9721-80f0bce00aa3 | -10.42214 | -53.83466 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5902bfe-1ce2-348f-b367-7dc319178d24 | -7.50665 | -55.03127 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a955410-d30c-3315-b0dd-d71e3055124e | -12.71816 | -46.98874 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 776d4c7b-b15d-3148-8c93-5fcc6a185c3e | -14.11158 | -46.29913 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 373e6e87-3fa9-32e5-a5c0-c83504184102 | -12.74894 | -54.05698 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2d4acac-80ff-3797-a32e-2bddd42eb6e4 | -14.22342 | -48.50945 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14a49ba5-b37b-39e0-8dcf-acd675e1c191 | -9.69038 | -58.12216 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5558274b-11fe-3f42-a2f2-a7eede5074cb | -12.30247 | -50.24501 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efa7574-48a4-3e5a-8d48-d794598a3265 | -11.43293 | -43.48107 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a022776e-4dbc-360a-b057-81866520a04e | -13.17705 | -48.527 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdcffc72-7a1a-3f93-a4cb-06325660de2a | -9.69097 | -58.11853 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44d3c73f-e7f8-35e4-aa65-fe1b30d87f46 | -9.07379 | -49.86813 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8faa0026-3d6d-3f2a-b84f-5f7d1b5c296a | -11.35354 | -54.0521 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16b5a5a7-84a5-3810-aada-6c5d23ea30b7 | -12.78807 | -54.01865 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37afed3b-c65d-3317-b307-cde2da24c52b | -12.80827 | -54.00829 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dd2ad98-1742-3741-86e7-6bd6aef2a90b | -10.3817 | -61.24837 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bed3ce89-4d11-32d2-a610-78905b212978 | -7.50889 | -55.03894 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4507b5ba-224a-35fb-898b-a6b1de5ae793 | -13.2209 | -48.55974 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aecfa0b0-939a-300b-b700-cb9dcf68e894 | -12.03585 | -50.93983 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b65a7df-b906-3701-b68c-25f848a5e36a | -12.94604 | -46.64965 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8c2b878-6faa-3a6e-adcb-c16dc42f81c7 | -11.38348 | -54.04821 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67f30402-5248-3fb9-b677-829b998bc573 | -12.71731 | -46.9959 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6dfd570-2112-3533-9384-3beda87ca4e6 | -10.39401 | -61.24588 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6445afaf-0ef1-35f7-9b55-6fd14e20dba6 | -13.53871 | -49.18173 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 468136ea-7725-3b87-a579-9c3b6d859e7b | -11.36133 | -54.04905 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 308dc0c9-4b49-3d17-8e0c-2c949e356510 | -12.7438 | -47.28133 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c5bc6eb-8ac3-31e0-83e2-32dbdf9bc8d8 | -8.8564 | -49.883 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 96f54ae3-75ec-32f6-956d-5c6f70701550 | -11.90648 | -50.6118 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b47f6fa2-88ba-3e07-b898-02351117cf54 | -12.01426 | -50.96739 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50c5f96e-a018-325c-8dce-35d1c33d68ff | -14.22304 | -48.51269 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 398cf300-899a-319b-b9c2-d4e24eba3747 | -10.26539 | -44.63847 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb400e14-4773-3b7a-aa10-567f00c3ce96 | -12.02651 | -50.9429 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a03c04c-bbb7-3dee-8a59-c3781a176c84 | -9.95566 | -50.15741 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bcbd24b-1369-3914-b3d2-7899c7f73ad2 | -11.42898 | -43.45269 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d795326-a176-35d9-81ad-5c89e605af14 | -13.16716 | -48.56429 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a10708af-2f04-307d-aeda-bb2cf33d9408 | -11.36912 | -54.04599 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0128a4f-c287-3fce-9936-812ed78c350c | -11.35211 | -54.11132 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75c868ed-e7ed-35ea-8d83-e3a2394fe7c4 | -11.42269 | -43.445 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6adff639-953e-35c8-8d28-ae02b3b9a0b7 | -11.89998 | -50.61389 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68b4a28c-169a-3ed1-b95d-b14e7628d45a | -13.08965 | -47.43966 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f64a331-fe51-336e-b853-b1e66f6f4862 | -10.8126 | -48.71613 | 2026-09-29 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92d14c36-5543-3eeb-bb99-28bce7d75ad8 | -11.34995 | -54.05154 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3e3d00-5604-3f01-aaea-d73b209f9a05 | -9.67105 | -45.55901 | 2026-09-29 05:12:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75e2bd1b-94bb-3d8c-832b-110c43c6261c | -7.50554 | -55.03841 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a905d40-e8a5-3065-9193-35ee34a21460 | -13.17276 | -48.56194 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89ae6429-54a0-3820-a909-37fb4baa6716 | -9.96324 | -50.13551 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89fc76d5-741c-3888-ab54-937060005bd3 | -11.35056 | -54.04741 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae214ab-511e-3160-acd4-a2e22aaace6a | -9.7901 | -48.19796 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f55790a-36e4-305a-b63c-51e44572a32e | -11.42805 | -43.48069 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| aa247a6c-a51c-365c-9d9a-6d7a48b6e01a | -11.4078 | -43.4505 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d89e68fa-dcdd-32c7-87cb-8e4893e1d0b9 | -11.18854 | -45.13649 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README64.md)
