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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a174ed81-00b9-3e97-9624-4bfe62b841ea | -24.17031 | -51.22937 | 2026-04-20 04:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| eebba2d0-0d9a-339f-b3c2-597fb7fe4fe2 | -22.49252 | -43.07219 | 2026-04-20 04:08:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 067ceef0-02fe-3fb2-b607-e702e2c86a2a | -23.54731 | -47.44795 | 2026-04-20 04:08:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 810bab1d-fd9c-3402-82ec-101178665632 | -22.49309 | -43.06844 | 2026-04-20 04:08:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7687b2ea-76b0-3c98-9dd0-f08339987e7f | -22.49194 | -43.07593 | 2026-04-20 04:08:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c578ba60-d04c-3d22-a5aa-1236cc0731ce | -23.64663 | -48.00129 | 2026-04-20 04:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a0ecdab-8023-3039-a5e5-777695a1d320 | -19.40107 | -53.35744 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33df8f59-429d-35fc-9b4b-b00c28126293 | -19.84204 | -45.01675 | 2026-04-20 04:08:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ab244e17-885b-3e2d-b393-d6fd63d89975 | -25.17509 | -49.39911 | 2026-04-20 04:08:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 02ad4d9b-82f2-384a-9232-3676a0785e49 | -24.17125 | -51.22482 | 2026-04-20 04:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 477dec6b-619e-30a9-816d-308df7408ad0 | -27.75528 | -49.97773 | 2026-04-20 04:10:00 | NOAA-20 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42289b67-971e-3f41-8f04-405b4e1a4b7b | -27.75428 | -49.97524 | 2026-04-20 04:10:00 | NOAA-20 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9b630850-04df-3059-9eac-dc381e240f6e | -27.75641 | -49.97202 | 2026-04-20 04:10:00 | NOAA-20 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a7833a7-7eaa-3499-9f21-522d9241aa15 | -27.7146 | -50.82971 | 2026-04-20 04:10:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6ed5f36-db41-3508-82d4-c6beefa564c8 | -13.63564 | -44.44365 | 2026-04-20 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9c4f174-3113-3449-be5d-179dcafa0555 | -13.4751 | -44.03202 | 2026-04-20 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7128732a-41cc-353f-bb18-bdf627681367 | -14.55198 | -46.93478 | 2026-04-20 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 566e98f5-4e35-3a88-93f9-5e5aba47d786 | -13.4695 | -44.03114 | 2026-04-20 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3c67a31-fcd7-304d-805b-691afea9fdcb | -14.55261 | -46.92971 | 2026-04-20 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03f823c-63c2-3162-8154-a8447de12b9e | -17.25122 | -42.66547 | 2026-04-20 04:55:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ad37942f-1be7-3484-8343-95eaa8fa778a | -21.9621 | -46.10852 | 2026-04-20 04:55:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bc156154-0268-3ec0-bd5d-81418b3c5c9b | -22.48561 | -43.07254 | 2026-04-20 04:55:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 685cf758-eac0-3df6-a9b7-680d697347a9 | -21.45167 | -56.15781 | 2026-04-20 04:55:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f362020a-2224-3113-aa82-55d2b3be94f3 | -21.45225 | -56.15411 | 2026-04-20 04:55:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0b80fde-6ea9-3c8b-ab46-092a8b49c889 | -19.84461 | -45.0173 | 2026-04-20 04:55:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 139bf5f1-0eda-3fbb-8933-daf7671dd51b | -18.58556 | -55.93669 | 2026-04-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b9c39c74-327c-360a-bc31-3726b02a239f | -17.82704 | -55.5079 | 2026-04-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cdba5700-0d54-3e37-85ac-89e2de1958d7 | -18.58614 | -55.93304 | 2026-04-20 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fd7d17af-cd0b-3ea8-ad6b-3fc2d2e01775 | -16.55131 | -49.91132 | 2026-04-20 04:55:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7971e04e-b65c-3def-a7d2-04d7d0da7c71 | -19.39988 | -53.362 | 2026-04-20 04:55:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8611da56-b0c5-3c8c-aae0-31ce797338a2 | -19.40045 | -53.35804 | 2026-04-20 04:55:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ad992c-0c28-3e01-a198-fec02b7e8ccf | -21.96177 | -46.11215 | 2026-04-20 04:55:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4be7f1cf-f2f0-3ac9-8e19-f81ce9464579 | -20.63174 | -51.70012 | 2026-04-20 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e387a1ec-83b6-309f-a31e-a4c3b4bbcb16 | -17.16868 | -46.83249 | 2026-04-20 04:55:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ebe018e4-f88c-3918-98d9-6e5124a3e594 | -17.25172 | -42.66016 | 2026-04-20 04:55:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bc611a1c-7828-3b05-84c3-038794d26751 | -17.16798 | -46.83843 | 2026-04-20 04:55:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5006e474-80f0-32b8-9b2f-8a20f404a49f | -22.49219 | -43.07314 | 2026-04-20 04:55:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 32c08163-5e97-3ae7-8914-aad5f351c91d | -16.31182 | -58.47882 | 2026-04-20 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77998637-4747-3191-a2d3-c323edf297f6 | -19.83889 | -45.01691 | 2026-04-20 04:55:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0ce9f52-0730-3019-88e8-f3c03d891ea2 | -20.03674 | -49.5983 | 2026-04-20 04:55:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b219d4c-596f-39b6-9c9c-d017b6722468 | -19.39644 | -53.36143 | 2026-04-20 04:55:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83b8ca5e-813d-302c-b657-03bed69e053a | -24.1765 | -51.23075 | 2026-04-20 04:57:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 1c46e18f-1adf-3264-a5a2-89a980352429 | -24.17229 | -51.22767 | 2026-04-20 04:57:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bee2eb82-d203-3b13-a055-cd1a577d6d09 | -24.17587 | -51.23208 | 2026-04-20 04:57:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ffafe6f0-c7f7-3163-b736-1ba0a02be140 | -27.75742 | -49.97269 | 2026-04-20 04:57:00 | NOAA-21 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4c9db77d-852b-3d19-bdf7-1403add015fa | -25.17479 | -49.39745 | 2026-04-20 04:57:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62d030ea-aaca-3509-81fe-18199b4c9056 | -24.17635 | -51.22818 | 2026-04-20 04:57:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 779689c2-c854-3acd-8b02-e90f6b89b2a2 | -31.695 | -52.74906 | 2026-04-20 04:59:00 | NOAA-21 | CERRITO | RIO GRANDE DO SUL | Brasil | 4305124 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 7198e854-d934-3c66-9b57-d321186e7182 | -19.39594 | -53.36059 | 2026-04-20 05:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9bb79be-2290-325c-816f-5ef3e6f9e02e | -19.40102 | -53.36134 | 2026-04-20 05:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 509b4921-1073-3f5d-af58-eb07d6d3dca8 | -17.88003 | -55.25407 | 2026-04-20 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9689c680-56e6-38d4-9be7-81ebf032760d | -19.40137 | -53.3582 | 2026-04-20 05:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a2df217-34ab-3986-a87d-f69f1ef8d8bc | -21.45089 | -56.15863 | 2026-04-20 05:27:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e10901b-3dce-38ef-8c53-003c2de5b9e4 | -17.87508 | -55.25788 | 2026-04-20 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e870b37e-e221-3722-99db-826821473b1c | -18.58693 | -55.93316 | 2026-04-20 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 494f2936-533e-3b20-ba33-2f536888d477 | -21.45041 | -56.15622 | 2026-04-20 05:27:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f973d4c7-787b-3103-a01c-e277746a730b | -21.4514 | -56.15419 | 2026-04-20 05:27:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95486ad0-9f41-3a28-a297-d768b0caaee6 | -16.31132 | -58.48114 | 2026-04-20 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 40ab4406-3074-3511-8eed-c1f3b15fc910 | -18.5864 | -55.93726 | 2026-04-20 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 97314248-2551-378e-9908-9fe87b512b10 | -21.45475 | -56.15688 | 2026-04-20 05:27:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc8b6855-574f-3127-9fd2-c9352bcb9de5 | -24.17541 | -51.22542 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a9cf57e2-2d34-38e4-867b-cccc55b4735b | -24.17024 | -51.2276 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d193667a-3d4c-3364-a938-b133f6e483e3 | -24.17599 | -51.23306 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d664c942-2ec9-363a-91ee-181bce7d88d7 | -24.16923 | -51.22513 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e3282fb6-0bfc-320b-b7f6-650adbf588fe | -24.17642 | -51.22788 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 75c93792-5033-3338-a52a-4a123f2f10b4 | -24.175 | -51.23074 | 2026-04-20 05:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 00f7aac1-65fd-3566-8c51-c91b702e7db4 | 2.76899 | -60.24508 | 2026-04-20 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb7057f6-8e24-3f77-98ee-6632a2073285 | 2.76712 | -60.24242 | 2026-04-20 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ffdc160-6034-3b17-820a-292553a9eab7 | -13.47233 | -44.0327 | 2026-04-20 06:01:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb59d998-7641-35ee-a954-7c60d1541b52 | -19.84106 | -45.01632 | 2026-04-20 06:03:00 | AQUA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7501c1a4-4318-3acb-8f5d-8f50151f3818 | -17.24753 | -42.66838 | 2026-04-20 06:03:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0e3b6729-1e7d-307c-be10-d2670f89d584 | -17.24889 | -42.6591 | 2026-04-20 06:03:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8118dddd-a761-34cc-9d91-3aedbc752191 | -21.23278 | -48.79184 | 2026-04-20 06:05:00 | AQUA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f372354e-f27c-3c20-b395-7d9151ee830c | -11.55441 | -48.26505 | 2026-04-20 12:21:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d43e5686-e559-3ab1-b4de-9d529b6b8506 | -15.10409 | -51.87596 | 2026-04-20 12:23:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4105eba5-dfbd-301b-be9c-8fbb04adb1d4 | -17.66873 | -46.73682 | 2026-04-20 12:23:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4cd2e3b3-032c-3fde-98a3-2ec9299bb36f | -15.101 | -51.86913 | 2026-04-20 12:23:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| db6b6428-1281-3d53-a26c-74b599b9fcbe | -18.67882 | -55.16188 | 2026-04-20 12:25:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 66102537-fc20-319b-a590-54e84e870b27 | -19.3883 | -52.98149 | 2026-04-20 12:25:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 063b319e-655b-399c-91b2-144a03f83014 | -22.96808 | -52.69435 | 2026-04-20 12:27:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 661005ee-e84a-3021-bbfc-87a95d603bb9 | -25.04978 | -50.04714 | 2026-04-20 12:27:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |


