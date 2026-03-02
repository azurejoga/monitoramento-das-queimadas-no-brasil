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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14bd770a-5cd2-3003-8c4e-c6e79456aa7d | 0.71276 | -59.51479 | 2026-03-02 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c406d37-127d-3caf-8cc1-97db545f0ee5 | 0.49209 | -60.50927 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 148bba01-2f7c-386d-b36b-89fbbd9d81df | 0.4982 | -60.51225 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb6476e-4c37-38e6-837d-828049609b7e | 0.47422 | -60.39429 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 254c4882-63d2-3cb5-a061-1b0b0c6f65e8 | 0.09168 | -60.6336 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dab25227-2751-330b-a19d-ba59e736936d | 0.46347 | -60.39414 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d584ba34-cfce-3f60-9116-c38258930d5f | 0.46898 | -60.39627 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0bbc031-bc6c-3c1d-b44b-ca54f2af80d2 | 0.92262 | -60.53107 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4c829b1-eb43-36a4-8523-ded6e2d7ded2 | 0.64498 | -60.6588 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a0c9788-9df7-3e45-86a0-46235046ea10 | 1.5046 | -59.9306 | 2026-03-02 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1660ba4e-a938-35b3-baf3-b2c65914e40f | 1.5047 | -59.9116 | 2026-03-02 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7ff9ce56-1159-3f17-8175-7d655a3edea9 | 1.5046 | -59.9306 | 2026-03-02 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f185949f-3309-3e07-99d5-12ce5e3cd699 | 1.4864 | -59.9117 | 2026-03-02 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 66250686-119f-3048-ab9e-d7b73948077c | 1.5047 | -59.9116 | 2026-03-02 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 2d6ed4a2-f9ef-3454-9160-50c75643f283 | 1.5047 | -59.9116 | 2026-03-02 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a1975fc2-d40f-30f7-b1b5-c9fc9c61ee68 | 1.5046 | -59.9306 | 2026-03-02 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1d619e1a-e8b5-3dc7-98be-2c2efe66efbd | 1.5047 | -59.9116 | 2026-03-02 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e0bf0c50-1283-336c-9a31-a8a777ccbd63 | 1.5046 | -59.9306 | 2026-03-02 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 92eeab82-5c42-36be-997c-8027ede3a4a5 | 1.5047 | -59.9116 | 2026-03-02 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8983aa2f-b48b-38a2-9d57-79d12da2518c | 1.5046 | -59.9306 | 2026-03-02 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 40f15c8e-abcc-3bb9-bef7-1ddedde31de0 | 1.5047 | -59.9116 | 2026-03-02 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| cb85ef1d-d892-340e-b199-addf44e9f29f | 1.5046 | -59.9306 | 2026-03-02 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2f15e31a-cb1e-3c37-a690-fc71540c8dd0 | 4.25789 | -59.90162 | 2026-03-02 07:33:00 | AQUA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 481eedd3-513e-39dd-a01d-677bad1a5d3c | 2.85461 | -60.8336 | 2026-03-02 07:35:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| efd30830-e9ee-33e9-bcbe-799f70deea68 | 2.86298 | -60.81986 | 2026-03-02 07:35:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| aedef450-26e5-3574-9f31-def3ab2e9d49 | 1.50009 | -59.90523 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 547307fb-1c8d-3e3c-acc0-292a19a77473 | 3.05574 | -60.66503 | 2026-03-02 07:35:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eca9e2e0-c8b5-3bf3-8863-bd71f3d50b47 | 1.86477 | -60.40017 | 2026-03-02 07:35:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6803b51e-45ae-34c3-875f-46eca0ed4e8d | 1.51141 | -59.90385 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8e4e2388-14a5-3dc5-a8bb-a64d5fe478f7 | 0.45588 | -60.38703 | 2026-03-02 07:35:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c9f71c28-2526-3665-b808-3eeb61e4f7c4 | 1.50237 | -59.92007 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 83d60f3d-78dd-3bc4-b30f-1d1fab9e07c3 | 1.47984 | -59.92343 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e5458abf-d2fe-31db-954a-43ce24a7be28 | 1.49109 | -59.92163 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 69706eb2-e346-3683-bf0b-035f6252a78d | 1.4888 | -59.90682 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8bad4835-e410-34ec-93b7-c5ff802b6e99 | 1.51367 | -59.9186 | 2026-03-02 07:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 55fe3e15-a429-322d-a622-598358e1c9fe | 3.4015 | -60.8357 | 2026-03-02 12:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 408286d7-61e9-34b4-82cd-4f93f28126d2 | 3.4198 | -60.8354 | 2026-03-02 12:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 38a6b703-ac0e-341d-bbb2-c87ba6806f6c | 3.4015 | -60.8357 | 2026-03-02 12:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 131.7 |
| fbeec820-0ac2-3b82-872c-f814951e839f | 3.4015 | -60.8357 | 2026-03-02 12:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 13f7665a-b66e-35d4-bb5d-cf8c7281b0fd | 3.0182 | -60.6907 | 2026-03-02 13:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3d0a2c76-e796-3efd-b059-4478f8a46601 | 3.4198 | -60.8354 | 2026-03-02 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 716f1e03-3821-3e4c-9e58-0a10a5329c9d | 3.4015 | -60.8357 | 2026-03-02 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 37efe67d-a132-3002-8af1-8345fa91aed7 | 1.5047 | -59.9116 | 2026-03-02 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 69e6f3bc-1c88-369e-88a0-53ace06fd122 | 3.2009 | -60.6876 | 2026-03-02 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f6a94c69-f8b1-37a6-9a71-4c29cce6c4b2 | 1.5047 | -59.9116 | 2026-03-02 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a32591b0-1c68-3ccc-80c6-c6f1f6034156 | 1.5047 | -59.9116 | 2026-03-02 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| af806e9d-84e3-3899-a3df-7ad62a5ab431 | -23.7189 | -54.9602 | 2026-03-02 13:50:00 | GOES-19 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 349af451-e225-3dc6-affe-eeb3c8ada247 | 1.1393 | -60.5222 | 2026-03-02 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 88b252d8-2d14-3818-b336-4e7b65efe72b | 2.8536 | -60.8259 | 2026-03-02 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| efd49a01-2f94-3d62-bee5-e8a2dcb794c8 | 3.0182 | -60.6907 | 2026-03-02 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 04092403-a49b-3382-8e3f-4699d7bf6a01 | 1.5047 | -59.9116 | 2026-03-02 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2fde0754-1c18-3485-9b87-6f9359f1564f | 2.8718 | -60.8256 | 2026-03-02 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4bec23d3-dcbb-35d6-b5ba-f7a9549ad328 | 3.4198 | -60.8354 | 2026-03-02 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1c82d3df-af8b-3aac-9cae-8fae5abe3c8c | 3.0182 | -60.6907 | 2026-03-02 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 124.1 |
| c1a3927c-8e1c-3544-a907-f33ef0779cfa | 1.5047 | -59.9116 | 2026-03-02 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fe6d5b3e-7504-32ee-ad3c-bcd0cbf50881 | 1.1393 | -60.5222 | 2026-03-02 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ce7ef746-bed3-386d-b16c-e66ef57acebe | 3.4015 | -60.8357 | 2026-03-02 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 245.8 |
| 217943e5-77b0-391c-8623-ff212e16cb2c | 1.121 | -60.5224 | 2026-03-02 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 438274ad-a686-329d-906a-f2c0f81def33 | 3.0182 | -60.6907 | 2026-03-02 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6876b0a3-7131-3a95-8193-23a360252ba2 | 3.0365 | -60.6714 | 2026-03-02 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8506a469-748f-34f6-a8fd-79e1138e1e30 | 1.1572 | -60.844 | 2026-03-02 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1fdf4205-db20-356a-a870-82a948d368fc | 1.1393 | -60.5222 | 2026-03-02 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e749f52b-31d9-3d30-be3a-2a0267c56e72 | 3.0365 | -60.6714 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9d7a36d6-c30c-39d3-8de8-ad71ae62cd1e | 3.4198 | -60.8354 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 58a175cf-e12b-36f6-9ed7-25bf09b73709 | 2.9999 | -60.7099 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| bc0ef6d5-2fe8-3f67-8016-bf5685d10089 | 3.0182 | -60.7096 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ea6691fc-1813-310c-a0fd-c8645c813278 | 1.121 | -60.5224 | 2026-03-02 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7636bc5d-3c66-3a97-9522-33509edf8aac | 3.0182 | -60.6907 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e159d571-38e9-3425-930d-38fc24003027 | 3.4015 | -60.8357 | 2026-03-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 942c91ef-84ea-32cf-8b96-95418a94f464 | 1.5046 | -59.9306 | 2026-03-02 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| adfa2f3c-dcf7-3627-b73d-113943b63dfe | 1.1393 | -60.5222 | 2026-03-02 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e9fab28f-7e9c-3282-abf3-8896271b5c09 | 1.121 | -60.5224 | 2026-03-02 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2149a045-97e8-3915-978a-2a690b0167ee | 3.0182 | -60.7096 | 2026-03-02 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 84cdcb49-ad9c-3031-89ec-83e4a00a6665 | 3.0182 | -60.6907 | 2026-03-02 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d339fedc-71fa-3372-904e-0d3c68d9dff5 | 1.1572 | -60.844 | 2026-03-02 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| babf3d72-ca0a-3632-8369-1287fd8e1d65 | 1.8689 | -60.4024 | 2026-03-02 14:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7d2ad85d-839f-3766-a653-dc7dd90bee8e | 1.5047 | -59.9116 | 2026-03-02 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 42d3eb4e-f5e5-36f0-864d-90bf8fea625f | 1.5046 | -59.9306 | 2026-03-02 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9e643c7e-bb48-3ed5-bd06-1e3cd5424859 | 3.0182 | -60.6907 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 521df813-d937-351d-8335-869a42ea2c11 | 3.1644 | -60.6882 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2ed47de4-90e3-3cc3-9d9b-3fb489edb564 | 1.1393 | -60.5222 | 2026-03-02 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f8e88a47-80cc-3eea-a76d-8bac4c94c19f | 3.4015 | -60.8357 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| aaa26b04-e6f7-34fd-840d-1e1ca35bc3dc | 1.1572 | -60.844 | 2026-03-02 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3f41138b-a38d-3803-86c3-9e20e1f403c5 | 2.8718 | -60.8256 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7018082e-9364-3123-9ce3-9854a015eeea | 3.4198 | -60.8354 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fe20d755-18b5-38d0-8ef0-2077933e98cd | 1.121 | -60.5224 | 2026-03-02 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ca6d2f41-84d5-3b47-85cc-d0ff934f8066 | 3.1826 | -60.6879 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 88af0c2f-fd95-35ce-96c1-134530039e5e | 3.0365 | -60.6714 | 2026-03-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |


