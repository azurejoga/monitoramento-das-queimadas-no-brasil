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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24d7fe24-5885-3f1d-ab30-b6c39f24156d | -5.97099 | -55.34966 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b24b41af-8c32-33d0-9f05-ff2637609d7b | -7.46066 | -54.97891 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70aa455a-72b0-366d-af8d-6e116162f4cc | -10.73397 | -52.03332 | 2026-10-10 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fab8ffb5-7b0f-3bd2-bb74-131c9c68e1a8 | -6.36654 | -55.27401 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1584e5dd-6df4-3c26-b053-f2db8ed54228 | -10.24426 | -49.68317 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd4523a1-bff4-3ac4-864e-1517042760ef | -9.20717 | -45.79401 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31f3b293-ebcd-3d57-9b3c-ecf277fb9a22 | -6.31756 | -55.32957 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8213a447-300b-3f90-9cd5-55ec528f698c | -11.87031 | -48.0344 | 2026-10-10 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc38e8f8-9eb6-3080-ad4d-fcc881457d68 | -11.68157 | -46.8549 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a4c0138-23b8-3afe-9885-d50c05eaa170 | -11.66728 | -43.70133 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50553ba9-6253-3c6e-859d-da37e1f86783 | -11.60158 | -43.69255 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31a76ae1-ceef-33e4-a7b4-0c34f00695b2 | -6.44007 | -55.04422 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56f526fb-bb9b-3576-89f8-32b5218705a0 | -11.98191 | -49.10442 | 2026-10-10 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb92cc90-c04f-30a8-a55b-afaff1479c31 | -10.46539 | -47.8495 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f01f56e9-2361-3c37-8dad-d0711b743d8d | -8.44895 | -47.98462 | 2026-10-10 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba46b3ce-4ad4-3f7a-a4d9-187aa1585288 | -11.60154 | -43.72284 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3eacc1ee-5757-3c8b-9207-532c83227fe3 | -7.61124 | -49.84401 | 2026-10-10 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37aa0a89-f151-35ac-8498-074b8dcff18f | -15.10606 | -43.63173 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dee86ddc-b554-3e35-965f-aca8c04c29ed | -7.52066 | -45.31345 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67372161-6991-3098-a368-9359eeb91573 | -13.91781 | -47.84718 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c61e179-2b90-3816-a0d4-472ceefe9acb | -6.73361 | -55.10618 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4232c6c7-0a39-3633-8b09-d502918203f4 | -14.5292 | -48.0447 | 2026-10-10 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b67d9fd-c4df-399d-9893-80db5daec195 | -7.23742 | -55.0779 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59df600d-ad80-3b50-a667-dcfa0808d4f2 | -10.04635 | -48.21463 | 2026-10-10 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c749f731-fe46-3a5e-b455-7424b574f32c | -7.0941 | -55.7337 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d85ac1a-879c-3820-8dfb-fb0db0cf5838 | -6.4651 | -55.49075 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d68ccd1-0aa8-3451-8d78-1a62d9732968 | -13.36787 | -43.8955 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125f1df5-ad04-3fd2-b2fc-f4ff0cbb0984 | -7.02225 | -47.66151 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cee76ec-693c-3771-b197-f991f86f9880 | -12.29395 | -47.04305 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 908033a7-fd80-3746-9bf2-2daa64559c00 | -6.04327 | -53.28596 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c43d8a3d-f429-3078-8d9e-ce941e6296ba | -7.91287 | -54.72606 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5bfa2e3-aeb2-3774-858c-8f79982baf7f | -10.52488 | -49.45789 | 2026-10-10 04:46:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6454859c-5381-3d23-bf4a-a1dbe57e9282 | -8.53381 | -49.56753 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02814824-d5e3-36c6-ab01-165fab59e324 | -9.71342 | -50.15215 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b589ac78-b910-374a-8739-63b763e157ea | -11.86751 | -48.03028 | 2026-10-10 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1349f32-bb17-3c0a-8b2b-ceb09d402530 | -9.09226 | -45.89079 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26e24952-7770-3408-93dc-26eefd52d8d1 | -10.89951 | -44.82154 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f53ae572-cd33-3afc-8cef-adb715eaf995 | -13.52855 | -48.43005 | 2026-10-10 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 688fa121-ee4f-3b07-95fe-8013ef3d11de | -7.7803 | -42.3108 | 2026-10-10 04:46:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 06b00ba0-0364-328d-9d8e-5095a694a874 | -7.00568 | -47.72309 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 875eb8ca-a22a-3b90-b8a1-dc6e1ca018a6 | -11.95837 | -43.50068 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cd84d9d-481c-3957-b15e-da3c1c02beaa | -11.38888 | -47.58508 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98bc6695-7697-3fe2-9b13-6e184f5b651c | -6.45299 | -55.28099 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 146fc048-68c1-357a-9fcc-ca29a2156099 | -9.27623 | -47.39671 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2119c37a-6699-362d-909b-0a6d15f1ce08 | -6.31922 | -58.31417 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b55ab78a-147e-3251-953d-e043be6375e6 | -10.25654 | -49.69257 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 949baf8e-30f7-3818-9962-fd1e1026e7b3 | -6.77459 | -48.66683 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 521c198e-a770-390f-a22f-017720560e09 | -11.80077 | -46.71042 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62757206-e1f3-3a91-a7ed-7220e0ff195c | -7.23733 | -55.16249 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a8dfe0a-3ffc-311a-ba6f-ecd646970a07 | -14.02002 | -48.76736 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5c9f681-6f75-35e4-ac02-004b0ef937c1 | -9.28743 | -47.39117 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f873463b-a1c2-3f9b-aa46-e64c9a45094f | -5.97584 | -55.35046 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 388123ce-e336-3923-9bb9-5aed44c8efc7 | -9.29241 | -47.39167 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ab2f42a-8bd0-39dc-b367-fca0c6dfcf8a | -9.12163 | -45.81509 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76abe079-7e11-3ad5-a8ce-d3c9b94366a5 | -11.80135 | -46.70652 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba108f43-f487-3495-af6d-003673e8a315 | -13.35769 | -43.89924 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e91ecf3d-f633-3be9-84c2-19d9bbb1449e | -6.47343 | -55.07565 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 725fbd44-67ad-3f67-9bcc-b791abfdc890 | -11.00366 | -45.40653 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56ce0c42-8adb-30ef-802f-f3d0416f6c9a | -8.49112 | -54.60795 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd33360d-17ba-3635-b4c1-ca8c4df3c3de | -14.45547 | -43.93561 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f34b2e06-4a75-317f-9518-c5de2717718b | -9.02039 | -46.86992 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c01d5aee-8ce6-36ae-abac-99a673c64034 | -6.36898 | -55.17136 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fd23914-4859-3139-9936-64efb58b90cd | -12.00099 | -43.43962 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3063e3b-1e40-3b28-b715-5b7010977d30 | -8.08388 | -55.28217 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1a713ef-e799-3897-b783-0423b9bfff89 | -9.27175 | -47.40335 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65388ff4-0021-3e58-af99-7d45d3dde06e | -10.90264 | -44.82665 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb04eb17-b3ee-377c-9581-52e99a33c3cd | -6.22689 | -60.03887 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1231c4ec-89e8-31fe-a1a8-3659c4f51be9 | -13.38185 | -43.88587 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a6902aa-cd75-339c-9361-fb2dc0f2acbe | -7.52008 | -48.02253 | 2026-10-10 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 25118198-907a-357d-a885-aaeab3455e19 | -9.22086 | -45.66248 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01164404-3965-3e66-8602-67687a103d8a | -6.21545 | -55.92169 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e1ac2c-7699-3cc3-b3e9-8602e172e9f1 | -6.37135 | -55.15874 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdabb0fb-63ac-3d4f-9122-656a37a26e54 | -11.57397 | -43.71087 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b202ac6-79fe-3ebc-9b12-f4b95c5d2756 | -13.19718 | -48.13904 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3abf3272-9dfc-366b-bd1b-63eed149a24c | -7.56365 | -45.64178 | 2026-10-10 04:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43dc8acc-8c60-344e-adb2-d0edd92358f1 | -12.05396 | -43.4008 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62a3bb75-17d4-33d3-9c8c-61163394a5bd | -11.58772 | -43.70205 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92692855-d0df-3358-b4b2-deffefde2049 | -8.25386 | -46.43308 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d0f1e6-37ca-3f17-8ee8-c68cd42c94fe | -13.38361 | -43.71317 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af2d6a7d-0408-3224-aa4c-6b26a3316406 | -6.67133 | -55.09337 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 566ac75f-98a4-3e53-9f8c-8f6b2be17d82 | -14.45758 | -43.95194 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70571c66-3fb6-38c8-9ebf-886bc2d3234d | -7.02613 | -47.65856 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b489149d-0ef6-3edc-a228-44c6f4383224 | -11.86147 | -43.54991 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f3bed59-bbfd-3a94-b410-3bafdb0e9b26 | -11.96424 | -43.48897 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5185bb5-0267-37be-86e6-212097dc7315 | -12.29741 | -47.04358 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6952f88b-cc2d-3078-810d-b0d75794fc37 | -14.32597 | -44.65697 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18d93e6c-ac5a-3c58-95f0-7f934de3980d | -12.36926 | -46.58702 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcfad8f3-7ee2-34ee-b729-250cc8e190c8 | -6.15158 | -53.30955 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fc93e4-2b77-3902-a764-686b7eb5b40d | -6.42373 | -51.95469 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c0b862d-bdb9-3e26-8fb5-d9093942bfd3 | -5.86414 | -55.70174 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5129788c-cca7-369d-8501-9fcd886077fa | -11.77796 | -43.52911 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a59a72c2-f099-3b21-aa01-b14688e928c9 | -8.65207 | -54.53567 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928ef30c-a3a2-32f7-b101-eaeefd21744e | -8.27211 | -46.42831 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5bb6090-45a8-3f98-ac67-a711b3708545 | -13.37099 | -43.90379 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c48b261-2957-362f-aa97-6e63e9460ead | -14.46231 | -43.9486 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa6781ba-25de-38a4-b78d-540823c9407c | -12.03504 | -43.382 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adcafa57-3a98-332b-808d-2df59d3ebfff | -13.35964 | -43.92552 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fecb7b96-3b2e-34af-a19a-6a63d7791fc8 | -11.76966 | -43.52789 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0caeb7a7-a9f3-3a7f-b2ed-d9e4ec4fda48 | -13.52978 | -47.4165 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 06814e71-ce1f-3e29-b9b5-24fe92d58ea4 | -6.45122 | -55.29136 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README85.md)
