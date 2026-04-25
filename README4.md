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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03297c51-7e2b-31eb-af91-878f6f04a116 | -18.35178 | -50.37677 | 2026-04-25 05:01:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 30f9d7c2-5806-3e70-903e-35ae354961b7 | -20.1553 | -46.85289 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5ec818a-bc6e-3a70-bfd0-7292739cf448 | -18.2919 | -54.13074 | 2026-04-25 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0919223d-99e9-3f75-8361-aec515417551 | -18.22773 | -54.59888 | 2026-04-25 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 504e6cbe-421b-332d-b98f-22bb07dd5394 | -20.18551 | -46.89387 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8b14b9-43dd-36dc-a1e0-41c49a835ae2 | -18.41643 | -54.54915 | 2026-04-25 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d81ca8af-7c55-3aad-8528-05a6e7f5446e | -19.45637 | -56.61419 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 38591a83-d507-37ca-86c5-2119f6f67f37 | -20.18735 | -46.87479 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 25b55234-1e33-304b-86f9-a7062889705c | -14.32685 | -57.72828 | 2026-04-25 05:01:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dffd2b9-ff16-3b41-b99b-9b6017d501b4 | -21.59959 | -53.84724 | 2026-04-25 05:04:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46a97a95-0270-3d8b-b3b6-cf71fb250ac1 | -23.37797 | -53.61773 | 2026-04-25 05:04:00 | NOAA-21 | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0702b5a9-10be-3938-9a3b-82be12b8112c | -25.46535 | -51.50888 | 2026-04-25 05:04:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a984e588-00a7-30a4-b412-21901d9c832e | -21.59898 | -53.85192 | 2026-04-25 05:04:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e03bf9f-b2fd-33e3-8ee6-61073c5b0b9a | -22.9699 | -52.69404 | 2026-04-25 05:04:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 03ddc376-7566-33b7-8e66-d48a60af819a | -25.17177 | -50.10709 | 2026-04-25 05:04:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf7b2423-a462-329d-bc41-396241db8851 | -25.23538 | -50.7301 | 2026-04-25 05:04:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07096c94-c855-33c7-b533-1d13bd6b8243 | -23.08144 | -48.61269 | 2026-04-25 05:04:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8af19e5-d002-3c6b-9d63-7ce197cf81f3 | 0.96872 | -60.40899 | 2026-04-25 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa661be-a81c-37a9-b383-19f29784323a | -11.84509 | -55.01921 | 2026-04-25 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e16c3314-d668-3db9-8648-b952a967ead8 | -11.84052 | -55.01852 | 2026-04-25 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff45d589-1bc1-3da4-a51b-048cfaa44e24 | -11.57377 | -54.5705 | 2026-04-25 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc987d08-d9f7-3922-bcfb-5faf832054ec | -14.20454 | -57.43279 | 2026-04-25 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37536fd0-7d4e-3a88-9a19-9a1017643357 | -18.50344 | -55.50769 | 2026-04-25 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8d06b272-66aa-3124-8d60-8a9de1351049 | -18.50408 | -55.50213 | 2026-04-25 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 40b7a5c8-de65-3db3-bf3d-bb38b915cd0f | -14.20955 | -57.42611 | 2026-04-25 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dbca834-ca34-3ef9-877e-09fd468d98a2 | -16.42407 | -54.92274 | 2026-04-25 05:33:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75478c7d-9438-3de5-bc30-3433404a2950 | -19.45801 | -56.61641 | 2026-04-25 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 05a9d342-e137-3817-add5-61fe5f3ca9d0 | -13.71938 | -57.48158 | 2026-04-25 05:33:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a82abe55-b2d8-350f-a3cc-b6d33e92930b | -13.99308 | -56.64727 | 2026-04-25 05:33:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3465c269-ed92-38ba-9173-9204ce2693bf | -13.7142 | -57.47957 | 2026-04-25 05:33:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7098cb09-2d08-3fc1-9f16-a271e32e8937 | -13.71744 | -57.48545 | 2026-04-25 05:33:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70dc20ae-a749-3250-8fa7-8e57ebe50190 | -14.20098 | -57.42877 | 2026-04-25 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0796968e-5c76-3a8a-a3f1-a30c5d9f2194 | -13.71539 | -57.48102 | 2026-04-25 05:33:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45626551-04ff-3642-ad97-d8a93136cffa | -13.99361 | -56.64334 | 2026-04-25 05:33:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 670197f6-b34b-35cb-8f2b-0feea553661e | -16.42284 | -54.92178 | 2026-04-25 05:33:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 108c12ea-779c-3ee3-bcff-9290efc2bc56 | -18.50893 | -55.50278 | 2026-04-25 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6610db3d-a99e-3350-94be-457615c3fe00 | -16.41917 | -54.92203 | 2026-04-25 05:33:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295adbe4-38de-3d91-bd48-278452548936 | -14.20502 | -57.42921 | 2026-04-25 05:33:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 782121b3-a9b3-3b2c-af59-a35759429baa | -22.97147 | -52.69565 | 2026-04-25 05:36:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9152a21a-1917-3452-90dd-33b41b657259 | -22.97066 | -52.69624 | 2026-04-25 05:36:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 22b74f82-5dc1-31f6-ba8d-56dd5b37cbad | -18.50647 | -55.50161 | 2026-04-25 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 91aa5a4b-4968-3843-91e6-a9801fdd727a | -14.20364 | -57.42956 | 2026-04-25 05:53:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d562048-3e42-3029-876e-a89850b34e0a | -14.19868 | -57.43151 | 2026-04-25 05:53:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2efce41-862b-3228-b4b5-cdbe63897ff9 | -14.2048 | -57.4316 | 2026-04-25 05:53:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5e43665-576a-3223-ad10-d98aba813ed9 | -14.21028 | -57.42524 | 2026-04-25 05:53:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4438f21b-478a-3cbf-89df-b1608af5481a | -13.65589 | -60.62896 | 2026-04-25 05:53:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f3da0ac-bef4-33d8-8ec8-a49fb217d79a | -13.99157 | -56.64901 | 2026-04-25 05:53:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 717ea486-02e1-304a-a5b7-69730cefb58f | -13.99211 | -56.64396 | 2026-04-25 05:53:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0682cc61-a9cd-324a-a637-f595b8c78d10 | -10.55522 | -42.44887 | 2026-04-25 05:57:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2e9b2520-c568-327d-bb2d-e3375dce6cd8 | -13.36895 | -45.29891 | 2026-04-25 05:57:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4a253ecb-6937-3cc2-8d34-2a32638e9b10 | -10.5568 | -42.43901 | 2026-04-25 05:57:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ae595c50-259c-3f30-b948-fc513ccc1a3d | -11.19928 | -52.55988 | 2026-04-25 12:21:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d044d3a1-fda2-3081-9653-a91817f70e44 | -12.99006 | -54.67649 | 2026-04-25 12:21:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f471741f-ef69-35b7-9323-7ff1fbfebc81 | -12.98872 | -54.68562 | 2026-04-25 12:21:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b7914261-6d12-3606-bcaf-316bf92c202a | -12.24251 | -44.16788 | 2026-04-25 12:21:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| f69aca37-b216-3176-8fef-78c00d406b09 | -10.58576 | -52.66903 | 2026-04-25 12:21:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b6b9e9d-7a03-3b10-8b0f-0321072a0518 | -12.70249 | -46.77955 | 2026-04-25 12:21:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| eb82257e-8177-3b6d-9f87-a95897003a60 | -12.08056 | -45.21942 | 2026-04-25 12:21:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| e5ba8240-6efb-32a9-bc2c-26486a774f1f | -13.99509 | -56.64764 | 2026-04-25 12:21:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 04c6df95-5350-340d-8366-4a5b12d439e6 | -11.60151 | -55.32875 | 2026-04-25 12:21:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3cb576ce-5230-32d3-98d6-c55571d73068 | -13.37156 | -45.29778 | 2026-04-25 12:21:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8bdba332-f172-37b0-8594-fc9c3577f14f | -13.67931 | -52.94077 | 2026-04-25 12:21:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e300b10-42ef-3d88-9dc2-ed74a02b94ce | -12.08231 | -45.21296 | 2026-04-25 12:21:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9a09a35b-db6c-3b01-868d-1dbcf6948b33 | -12.0672 | -45.2115 | 2026-04-25 12:21:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 056e1d4c-2304-3fed-8851-473ef766c388 | -19.95158 | -54.38145 | 2026-04-25 12:23:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d3d1183-5e51-3845-9baa-71b9d66c32dc | -19.95026 | -54.39107 | 2026-04-25 12:23:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b4bf340-de4f-3d92-bccf-2cabbfec53d8 | -23.67758 | -49.83636 | 2026-04-25 12:25:00 | TERRA_M-T | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 7d99966b-4ca9-3a51-a8a5-bcf46e00d352 | -13.3955 | -45.321 | 2026-04-25 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 298a6fda-9a85-33eb-9028-e46badfa9661 | -12.2421 | -44.1807 | 2026-04-25 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 20ed6fd0-b026-34b9-9e19-8f950e0138b6 | -18.512 | -55.5022 | 2026-04-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 6d5f64ea-5c4d-3d73-8be2-484bc6a8871e | -18.512 | -55.5022 | 2026-04-25 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 4c198aee-6a0c-329f-b41c-251a2ab246ce | -12.2421 | -44.1807 | 2026-04-25 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 76b0127a-9e00-39a3-b86a-e78ff48ca567 | -18.512 | -55.5022 | 2026-04-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 1645f88e-b3fd-31d7-895e-dc4b37aba352 | -13.3955 | -45.321 | 2026-04-25 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 41dbe937-a226-30e2-af1a-85d77e2f1b76 | -12.2421 | -44.1807 | 2026-04-25 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| d63ecf64-dd08-3e6a-9e91-53f4927681f4 | -13.3955 | -45.321 | 2026-04-25 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 633ab28c-2e5c-38c8-90e0-965600f04076 | -12.2421 | -44.1807 | 2026-04-25 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| c85485cc-12ee-3b74-ba41-4d80cbdd74c7 | -18.512 | -55.5022 | 2026-04-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 82d913c7-d960-39ef-a026-310c5cf9853a | -18.512 | -55.5022 | 2026-04-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 19e93fc6-902b-3a42-ae5b-1b47b0fd5bb7 | -12.2421 | -44.1807 | 2026-04-25 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 1fa9ed12-c5da-3168-9e93-0899f28baa59 | -18.4921 | -55.505 | 2026-04-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| b8ffdb78-6576-3baf-b743-1eba05eff430 | -18.512 | -55.5022 | 2026-04-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 20e7dfd3-b9c6-32d2-9762-5b63b0f40e93 | -18.4921 | -55.505 | 2026-04-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| d656cf8d-9119-3641-a685-015a2b5f4b8f | -18.5116 | -55.5232 | 2026-04-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| b54e6bb7-0fbc-31bd-9248-b42e7da0b0f0 | -18.512 | -55.5022 | 2026-04-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.9 |
| d06e7458-ee10-3713-855a-c272e75fa548 | -18.512 | -55.5022 | 2026-04-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.7 |
| 9d202d56-d7de-3147-987a-2329048b19f2 | -19.9543 | -54.3899 | 2026-04-25 14:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9be1ee8c-b0a3-3e8d-81b5-8ac0c00218e2 | -12.2421 | -44.1807 | 2026-04-25 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ba40359e-a4a4-309b-a5c4-e8159a8db8c4 | -18.512 | -55.5022 | 2026-04-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 11d41813-8f1e-337e-a827-b34489034309 | -18.5116 | -55.5232 | 2026-04-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |


