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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed76e501-84cb-3e2d-8203-de9d8a876916 | -17.03309 | -57.50271 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c8601650-28ac-37b6-8ce7-9873d666ed47 | -17.03296 | -57.52048 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 27fdb639-0b70-30f2-9a56-7534f597c6c1 | -17.0324 | -57.52687 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a8fa897a-aaa0-3f73-ab20-0801ce6e2747 | -17.0313 | -57.52182 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 38f69a32-d00b-336b-a78c-d1ae4b8796a3 | -17.0307 | -57.52818 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ac46684c-9cfc-322c-9ea6-6b69cf63d4f4 | -17.02781 | -57.50054 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7f490fe8-79ab-3bbd-9b44-42d414a16f17 | -17.02628 | -57.50195 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| dfd04537-cd44-3876-9a6a-2b53ff70bf81 | -17.02559 | -57.52609 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a1871928-3790-35f5-84bf-dae6b1250b4e | -17.02449 | -57.52108 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 37ec3f59-bc73-3f4c-8bb3-f80df744c75c | -17.0239 | -57.52745 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f8891326-bd9c-32c5-9101-7a8746c35571 | -17.01879 | -57.52532 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 77084d64-19fb-3931-b493-c331fbb8ef48 | -16.97571 | -57.52847 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 74db7436-d399-345c-898d-28549f8fc355 | -16.97513 | -57.53482 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 332685b3-69f0-3447-a13c-02db433ba6d0 | -16.96891 | -57.52769 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 9be82553-2932-352a-a964-d6e7a8b13626 | -16.96211 | -57.5269 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| b5667c57-e6b7-3bb0-96c3-10d8c9ca739b | -16.96023 | -57.52588 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 9ad8dccc-403b-371b-9fdb-2cd613c5ca31 | -16.94059 | -57.5373 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 74755ab6-8207-3fbe-abc1-ae2b7f7dfb77 | -16.93863 | -57.53632 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| a20d52c9-9de8-3059-9f72-6181c98fcb72 | -16.93548 | -57.51744 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b8b32621-ff4d-302b-a088-312f33ed6d6d | -16.93436 | -57.53016 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 5238c7cd-4ce4-3ed6-82fd-1e2132141e97 | -16.9338 | -57.5365 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b03c4f3b-0d7e-3bb0-9755-dda459071fee | -16.93364 | -57.51653 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9aa884cc-e1ca-31dd-a20b-727f10dd7ce9 | -16.93304 | -57.52288 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 96bb20e5-f23d-3a78-b766-3dc54f5e15ab | -16.93244 | -57.52922 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c39fd004-bed8-3f48-89f1-155758eb22e0 | -16.93184 | -57.53555 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| baeb6693-cceb-3040-804b-ac18b386a1cd | -16.92867 | -57.51667 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9c9f1188-9d05-300f-914b-cbd59f70a320 | -16.92812 | -57.52304 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e569bb60-950c-3623-919b-8353c3fb43a8 | -16.92756 | -57.52938 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 84cdef38-6aff-3799-b3c4-55513787604b | -16.92684 | -57.51576 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cf95ca87-1ee8-3aa0-870d-953247519be6 | -16.92564 | -57.52847 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 556f8eab-8523-3a93-93cc-ac0d76601eeb | -16.91618 | -57.50233 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 079fbe50-9937-39b2-9080-00c46f99de29 | -16.91442 | -57.50152 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5e6138f7-d20a-3c6c-a99a-a5078df97c80 | -16.90762 | -57.50077 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2d3a39e7-60bd-3f3c-957f-09a216e7b288 | -15.0359 | -59.70514 | 2024-10-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e4e2c9d-815e-3875-abd1-545651f5484a | -15.03568 | -59.70568 | 2024-10-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80ee3102-74ef-3e8b-aed2-af7a39945b7d | -15.03007 | -59.70443 | 2024-10-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccf5b36c-e159-39b5-b712-c4f226a0fb85 | -15.02985 | -59.70495 | 2024-10-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eeb9fef3-bce4-358c-bd39-b1e825f77da4 | -15.93354 | -59.57018 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00e271fd-c33b-3b8b-9116-f50777aca096 | -15.68591 | -59.74035 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b765dbd5-2615-30ef-84c6-f9a9bd7d99f5 | -15.68546 | -59.74466 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5609d4f-4b11-334d-9faa-8fe66dec58b8 | -15.68004 | -59.73961 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b7f6df8-dd71-34b6-a8cd-fd84048470b6 | -15.67959 | -59.74394 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e964f3-baba-3b45-8e80-6b3a91ffb88c | -15.67504 | -59.73853 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 283fd70e-9a03-3167-aba5-feb470f77061 | -15.67456 | -59.74283 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a07ca05f-90fd-363c-a210-92c620804b02 | -15.67418 | -59.73889 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7057c1c-26ec-3655-9755-49f09b0d4314 | -15.67408 | -59.74715 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53bcfb7d-28ff-36e8-a0e1-7d2a995d3656 | -15.67373 | -59.74321 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d15f88c-faf0-3623-87e0-e70dcd49ee87 | -15.67328 | -59.74752 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb86dbf3-bc1e-3753-a89c-a00a0d1449e5 | -15.66822 | -59.74643 | 2024-10-25 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53a1e03c-051f-3745-87fc-7a4b5122f636 | -12.05457 | -63.14513 | 2024-10-25 05:57:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96077c44-5142-323b-a4cb-015ae3428c3a | -12.05086 | -63.14651 | 2024-10-25 05:57:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb8ebdd8-f53b-33af-9ffc-238807ea9d76 | -12.05012 | -63.14449 | 2024-10-25 05:57:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d0f874fe-730d-319f-bceb-2fa247ae1165 | -12.04641 | -63.14588 | 2024-10-25 05:57:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43d315f8-8e9b-39c9-b401-7050154682ea | -12.53256 | -63.05853 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 865a1297-4933-3563-abe6-67090bdbdd76 | -12.52806 | -63.05789 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c73138f8-ae55-3d44-bf40-a179d4261ea3 | -12.52355 | -63.05725 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73c5ec73-3fb5-35d8-9184-576c99fe569b | -12.51904 | -63.05662 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255904d9-870f-37f6-a209-323b6e409a92 | -12.47079 | -63.15996 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f3a175a-fc9f-3d18-8561-4035e852c604 | -12.47018 | -63.16447 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca4d7078-2148-322e-b4be-07d18882a20d | -12.46957 | -63.16898 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 147e6d50-0782-3543-9696-f5275e68fc9b | -12.46906 | -63.16115 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff9d9ab8-8d11-3868-92b7-676a3d599564 | -12.46849 | -63.16568 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccdf7951-3fbc-3742-b3ea-c1be04b8a532 | -12.46791 | -63.1702 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 056fc81e-ee02-36e8-b619-177bd948633f | -12.46632 | -63.15933 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58dd468d-9039-3472-b829-d4e08d247d86 | -12.46571 | -63.16385 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5832e6d-b498-3290-b3c5-d10f07c55966 | -12.4651 | -63.16836 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4166dcb2-19c3-38a6-98ae-550922f3d4d1 | -12.46459 | -63.16053 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e64201a1-8a9c-3524-ada8-1724681898fa | -12.46449 | -63.17288 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f962ad75-800f-3d67-ae9c-e87d5f3fee2b | -12.46402 | -63.16505 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b131d21-8045-3eda-9e0a-b5aa1ff4cd60 | -12.46388 | -63.17738 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a697df9-676f-3466-bf7d-e364144a4bbb | -12.46344 | -63.16957 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82fc2aba-6f0d-3621-8c35-a8698dcf20f3 | -12.46287 | -63.17409 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7a5a08c-5df6-3334-8bf9-623fb70bec51 | -12.46229 | -63.17862 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0d388b2-924f-3003-b778-e54cda25725a | -12.46063 | -63.16774 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bf038e8-1413-3e12-a453-e1de2f527f5c | -12.46003 | -63.17224 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d66f195e-d699-341e-9170-881a68902c10 | -12.45942 | -63.17676 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4597e82-89fd-35da-87c5-2aa12b807a3c | -12.45881 | -63.18126 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f90af5b9-2d71-34db-aeb2-44f8c2bb0a5d | -12.45435 | -63.18064 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1298a342-cc66-38e0-9bb1-2e8b83df5dc5 | -12.45374 | -63.18514 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b535098-a49d-38c2-8084-3ef4dd10a892 | -12.45314 | -63.18963 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83eb0d80-fc1c-3492-8827-7d36b5d1f581 | -12.45254 | -63.19413 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89a2e350-fdb7-3487-afea-625822250ca1 | -12.38527 | -62.93731 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0454942-9eef-3549-87ba-e5f1ae7ad473 | -12.38379 | -62.93904 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5007e725-f3a3-3103-9a17-1e3b1c175211 | -12.8366 | -62.87583 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34e04f0b-76dc-3088-9753-868d31877b13 | -12.8365 | -62.87728 | 2024-10-25 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0969931d-2ac7-3109-89f4-f3abc47fe6fa | -12.38242 | -63.87096 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f24ff2b1-21e8-3c66-9cd8-a1d89571f51b | -12.38218 | -63.86886 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9442243b-bf7c-3e1c-9520-5fa75dec11e7 | -12.38186 | -63.87502 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ff8a0de-417c-32a1-b520-815ccd39e588 | -12.38165 | -63.87292 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c69346ec-cfb0-3cbe-a7f3-36d6be4a5a59 | -12.37928 | -63.86227 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0fbd697-e344-3a8e-8e52-36c99c529958 | -12.37898 | -63.86014 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c0f789-db40-3bf5-a350-3eff5063ec15 | -12.37872 | -63.86633 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8ab256a-a1b0-39ec-921b-2af73c787f1c | -12.37845 | -63.86421 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1f43d2b-6f89-32ef-818f-be20a16fd343 | -12.37502 | -63.86167 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6703cf92-0ae1-391d-a1bf-09413ffda204 | -12.37472 | -63.85952 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f293ff75-8f3b-31fe-a135-b5e536a6f173 | -12.37446 | -63.86572 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58262a72-9612-351a-99b9-3bdcdb8aa0d1 | -12.37419 | -63.86359 | 2024-10-25 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b998d04-19a0-37c2-8b9a-8b8394a3415f | -1.6062 | -53.3087 | 2024-10-25 06:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 29b8e253-8284-3c3b-936c-0368c54d9187 | -2.74714 | -67.02306 | 2024-10-25 06:18:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36fa03fd-7810-36e7-a0ab-13d7792b8c07 | -4.51608 | -61.13715 | 2024-10-25 06:18:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README111.md)
