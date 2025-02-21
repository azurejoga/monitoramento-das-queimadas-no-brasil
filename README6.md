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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f8bf794-7c8b-34a9-9669-ff6ef65133a2 | 4.00886 | -60.87284 | 2025-02-21 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d77e58a-25d5-3840-b8d4-bd087434eb26 | 3.14675 | -60.18421 | 2025-02-21 05:20:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9c07b43-6197-384f-b1f0-483fa41e96bc | 2.51037 | -60.98085 | 2025-02-21 05:20:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e992767c-91c7-38ab-8474-0d82757b7f00 | 3.15014 | -60.1837 | 2025-02-21 05:20:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad06add4-3893-330a-84ba-e2bcb519a0cb | 4.18097 | -60.17822 | 2025-02-21 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379fb486-95b6-37be-aa0f-84be9b602e1a | 4.00777 | -60.87212 | 2025-02-21 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae079098-4886-3ddc-8f13-8fe39351b918 | 2.66896 | -61.40339 | 2025-02-21 05:20:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5540ce67-18ca-3121-93e4-8974608fe57a | 3.14731 | -60.18787 | 2025-02-21 05:20:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29ba1a94-1faa-3e81-987a-b50175f7d5b9 | 3.15298 | -60.17954 | 2025-02-21 05:20:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36fb020a-920c-355c-ad07-a1b97b6ead9f | -6.97705 | -43.00641 | 2025-02-21 05:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7fb87391-ad2c-3491-a7cc-e8528ff685d1 | -6.97572 | -43.0154 | 2025-02-21 05:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 870de0ce-1f82-3adf-bcf0-d92c3283862d | 1.71619 | -60.72047 | 2025-02-21 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9168bbad-c9b4-3b8d-84ef-543531af00a4 | 0.82505 | -59.94947 | 2025-02-21 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f00c1ca1-123c-31d9-b6fa-11f6fd77df2a | -9.12606 | -61.46703 | 2025-02-21 05:22:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 626428a3-a1c3-3748-bfd7-6962c7eb73a0 | -11.18484 | -54.40528 | 2025-02-21 05:22:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2922e4a-2111-3a54-a9e1-01fa8073575c | -12.10299 | -51.22946 | 2025-02-21 05:22:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd102c98-e87c-398a-a9e0-26bda8b71cc9 | -11.18651 | -54.40419 | 2025-02-21 05:22:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51cc2d02-9a6c-3642-9923-46ef3c89ee3f | -2.1601 | -53.65335 | 2025-02-21 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b650532e-32b3-30cd-99ca-b430b16af4e0 | -8.75193 | -63.47328 | 2025-02-21 05:22:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e519667-fc17-36db-b2f4-7f3c8d772f48 | -17.0479 | -45.04019 | 2025-02-21 05:25:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8bdd7c3d-d14e-3f89-829d-0ad61266ef99 | -17.45656 | -47.00335 | 2025-02-21 05:25:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f085c6ae-3a64-39e8-9981-3f88ec213d19 | -11.85677 | -46.94012 | 2025-02-21 05:25:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33e1005e-886f-3a03-a06a-aaaf355cfeab | -14.43348 | -45.63344 | 2025-02-21 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2918551b-10f6-39f0-8b82-059d774831d4 | -12.79997 | -45.00566 | 2025-02-21 05:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0cbdc23f-c48e-34d6-867a-a79f31c6b9a9 | -7.71966 | -55.20731 | 2025-02-21 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5204ab4a-293d-33ae-a7da-f47f9272160e | -12.34847 | -64.22215 | 2025-02-21 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e278f95-6c07-3201-ab81-b84f2c95988f | -19.09005 | -56.06344 | 2025-02-21 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9a896a42-01e9-3e8f-8e22-65f92fddf338 | -15.53951 | -60.10984 | 2025-02-21 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d8c24f6-f7e0-3c3b-8ee0-889b48d65d0e | -19.08541 | -56.06283 | 2025-02-21 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 19b0c1bd-2a81-3b06-bccf-9514c1c13a85 | -12.34782 | -64.22602 | 2025-02-21 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a5ed8bc-8400-3354-b810-c232a64cc4c7 | -12.27651 | -63.7406 | 2025-02-21 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c570ee5-582a-3e29-8efa-1445266033ee | -12.35193 | -64.22273 | 2025-02-21 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 897f859b-024c-319a-8edd-3f7964f4a095 | -12.34501 | -64.22157 | 2025-02-21 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92954e25-08a2-3bda-8194-e24d5e9aa090 | 1.7147 | -60.72117 | 2025-02-21 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fd7d2b2-9a3f-38f3-b1d9-71dd7f32b040 | 2.50888 | -60.98192 | 2025-02-21 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acd99400-ff0c-3dae-838c-20225fd8ede6 | 2.2498 | -60.29274 | 2025-02-21 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2024b32-882b-39ab-9aab-b98072337940 | 4.18132 | -60.17757 | 2025-02-21 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b92bf05-62bb-3017-8b86-af92256f0c9e | 3.14962 | -60.1846 | 2025-02-21 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed090127-113b-3679-be43-9d7b6199f12a | 3.14648 | -60.19027 | 2025-02-21 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a4c0a38-4dc1-3cc2-92aa-9e0b27a66369 | 1.7186 | -60.72055 | 2025-02-21 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 087683a8-e8a9-38c0-b1f5-8aba8e6e2603 | -12.27552 | -63.73983 | 2025-02-21 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 210766b6-2827-30c3-a2d6-fa23aef3949f | -12.34596 | -64.22572 | 2025-02-21 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfa8f406-6543-3055-9ae3-909a8229dff3 | -12.35045 | -64.22155 | 2025-02-21 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c19ea7e0-9e52-33b8-9b6c-3288b8b9d3a4 | -9.78663 | -64.80173 | 2025-02-21 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4da4958d-6bea-39de-a0c2-2084928a5f58 | -12.34664 | -64.22098 | 2025-02-21 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 061122a4-4d5b-3ca7-9093-dcda84f0bdce | -9.78601 | -64.80585 | 2025-02-21 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50950aa2-38a7-32ec-9968-2af468262d4d | -19.09318 | -56.06132 | 2025-02-21 05:52:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8aaf6f55-d275-36da-bf5b-93f5c2fb1322 | -19.08619 | -56.06066 | 2025-02-21 05:52:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 64105014-be20-3cb9-ac8a-48ded68c7013 | -19.09262 | -56.06816 | 2025-02-21 05:52:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7422d3e3-79df-370f-be4f-7aa206b5ea63 | -19.08563 | -56.06749 | 2025-02-21 05:52:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3e6b0c7e-972f-3b21-a84e-bbcf2e7aa956 | -12.823 | -44.9975 | 2025-02-21 11:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 9c6dbc59-4817-3fcc-b025-409281107f0c | -12.823 | -44.9975 | 2025-02-21 11:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 30224910-4800-3728-8af1-ad155a53436d | -12.823 | -44.9975 | 2025-02-21 11:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 5b6b77a3-b799-31d5-911e-eada2078d454 | -12.8037 | -45.0006 | 2025-02-21 11:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 450031a0-fa8f-3aa8-9a86-17812792a956 | -12.823 | -44.9975 | 2025-02-21 11:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 5ca7d2c0-ff03-3ce1-be99-572123fec65e | -12.8037 | -45.0006 | 2025-02-21 11:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ff5180c5-a888-37d4-b7fe-83070adfbef2 | -12.8037 | -45.0006 | 2025-02-21 11:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| af3bd3c9-86ff-3c48-b378-332c44c7e449 | -12.823 | -44.9975 | 2025-02-21 11:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 1f9b73a1-6d69-3bba-8ddf-fbe50a3a00ab | -12.8037 | -45.0006 | 2025-02-21 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 4f4e46a8-9069-33fd-ab37-2b9d091f9ff8 | -12.823 | -44.9975 | 2025-02-21 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7e127bb2-6681-3f20-95b2-02744570e229 | -12.8037 | -45.0006 | 2025-02-21 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| fc2abd41-6499-33db-9b14-d544da73f962 | -12.823 | -44.9975 | 2025-02-21 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 5a806da5-882f-361b-a5df-73ba3e84d6e5 | -12.823 | -44.9975 | 2025-02-21 12:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 49e4dc4c-ba5e-3e61-b884-8bbd742c978b | -12.8037 | -45.0006 | 2025-02-21 12:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 5e8438cf-9a64-3b13-a410-d6dd30b286df | -12.8037 | -45.0006 | 2025-02-21 12:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 4d358540-0154-3c1f-8222-1c13afd53cad | -12.8037 | -45.0006 | 2025-02-21 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 200d5ead-1a79-336d-8944-33f13800a021 | -12.823 | -44.9975 | 2025-02-21 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 6f7afba6-9881-39fb-8e0a-d2f43fad544f | -12.8037 | -45.0006 | 2025-02-21 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 70d2b58a-a6ed-394d-93db-a9b562adf9a8 | -12.823 | -44.9975 | 2025-02-21 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 302cda87-fa6c-30ee-9cd0-093c048261e3 | -12.8037 | -45.0006 | 2025-02-21 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 247.2 |
| aac4baef-dd77-3a0d-90ed-1938b19c09ec | -12.8037 | -45.0006 | 2025-02-21 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| db600819-c310-3d7c-880b-2f03269b7b84 | -12.823 | -44.9975 | 2025-02-21 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| cd3d2580-711e-31f2-9b93-e2c31560331e | -12.8226 | -45.0208 | 2025-02-21 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5b6031b7-41a8-3592-b6a9-c46b36eb6149 | -12.8037 | -45.0006 | 2025-02-21 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 30c9e03f-9aef-3524-83a1-81aa5df4423c | -12.823 | -44.9975 | 2025-02-21 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 74016f0a-fef8-333d-a5b8-2d483333bd07 | -17.0609 | -45.043 | 2025-02-21 13:30:00 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 33b36c3d-67cd-30c0-a537-494bf5c60f3c | -12.8037 | -45.0006 | 2025-02-21 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 43989845-fb9f-32ec-af41-09035eae343a | -12.823 | -44.9975 | 2025-02-21 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.9 |
| bdaa8eb8-df29-3ea1-a4b5-2f44e1ba618f | -12.823 | -44.9975 | 2025-02-21 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| a3c72a42-550c-3327-8737-daffa8269b13 | -12.8037 | -45.0006 | 2025-02-21 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 5f4344c1-5fbf-39ad-bc78-43980438caab | -17.0609 | -45.043 | 2025-02-21 13:40:00 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b148a64f-b9f5-3415-9dcc-9f8d58b6250b | -12.8037 | -45.0006 | 2025-02-21 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 835772e2-04cf-3780-8dab-6d5984403a62 | -12.8037 | -45.0006 | 2025-02-21 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 12476b55-472f-3515-9a40-191bd5f83bac | -10.4324 | -44.8848 | 2025-02-21 14:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 32adac42-c619-3918-903f-afca82510291 | 4.0046 | -60.8807 | 2025-02-21 14:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 41db19b4-eaee-3150-99db-45d0225e6276 | -20.401 | -48.5319 | 2025-02-21 14:30:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c45ec580-2a99-3722-95ac-c97622a97dd9 | -20.0663 | -48.1452 | 2025-02-21 14:30:00 | GOES-16 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |


