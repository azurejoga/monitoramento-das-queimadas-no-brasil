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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75e4920a-8865-3865-ba7e-0702306b61cb | -12.30853 | -59.18254 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f124e85-7451-3eb0-b093-de583a8df1f1 | -12.30783 | -59.2297 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4821e9c3-3419-34a1-8f0b-e6beae7404d7 | -12.3072 | -59.23353 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f32687c-7be2-3513-884f-2c0024378dea | -12.30572 | -59.17816 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c8d307b-fd39-3415-a30c-c5929a2d450e | -12.30439 | -59.22909 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77773f04-4f5f-34c8-ae2f-f5b6ea8a7d22 | -12.29353 | -59.18785 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b230544a-7713-3aee-9a0a-0c33afe2067b | -12.29072 | -59.18347 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4aa728e-0e7a-37f7-a100-b8362142a972 | -12.29009 | -59.18728 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a9ff0d0-30ba-3449-85e7-10ae08632e97 | -12.24454 | -58.93068 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cca8ace-e70d-322a-bffb-12253f35d8dd | -12.22128 | -58.92296 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61035124-794d-3726-85ef-26bf8854d70f | -11.8842 | -59.03041 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feacaf68-463f-32c5-8189-78007da8f605 | -11.88141 | -59.02596 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6eb053ba-be47-3714-9f67-4cd17cc7a7e4 | -11.88078 | -59.02979 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd6decc5-ba6b-323a-9a65-1d72165b1902 | -11.87799 | -59.02536 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5600473d-66e7-37df-b4db-714b71bfb3ed | -11.71167 | -59.14358 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5472b361-d38b-3656-8d48-1a1f8649af9b | -11.71072 | -59.12764 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501cfbec-5832-3182-b07e-c7c97056382f | -11.70728 | -59.12707 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d197e4f3-fe2b-30f2-ac7d-484612f249d5 | -11.57401 | -58.95246 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6646a641-3966-389f-a771-af9da9c8ee25 | -11.57339 | -58.95626 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a94c1ec2-0fbe-38af-8431-acd861405f87 | -11.57058 | -58.95188 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e8b5d64-b874-3bf1-b186-fac81da7a393 | -11.56996 | -58.95567 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be261c48-3dd5-3bec-a643-7c10a0ef9d71 | -11.56653 | -58.9551 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94563133-fef5-321c-95fc-d81b4b1df560 | -11.56247 | -58.95832 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579b84bd-c2be-381e-b359-48f44f2bb69b | -11.56226 | -58.61617 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4845a3d6-c79f-3b5d-b24e-638ad7a23c50 | -11.49064 | -59.09984 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1902cf0-9dfa-3419-a06d-9ef5e40a012c | -11.48719 | -59.09925 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fd82512-5ae5-30ac-99da-940e56036f94 | -11.3774 | -59.1922 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a511b3a0-fe59-3bdc-b072-1b86c290bd4e | -11.3703 | -58.9969 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb72709e-8f09-37a5-a392-3864599ef1a6 | -11.36686 | -58.99633 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47ea0501-003b-381a-bf53-20ae51f6fe3e | -11.34686 | -58.98894 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0277bb97-2a75-327b-9a8c-80f3213d89d9 | -11.34624 | -58.99273 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9683cfed-e5f4-3875-88fa-d1239325fdb9 | -11.34343 | -58.98835 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04fd0556-ea3e-3d4a-b108-8faf2265d2db | -11.3428 | -58.99216 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe247eef-c137-3e9e-be5f-36e5d8ecd00b | -11.33999 | -58.98777 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34285e9d-9905-3e9a-b903-0cb332a59e44 | -11.33936 | -58.99161 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fbe25d5-893f-395c-b0d2-bf0529d73e17 | -11.33409 | -58.91669 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6259ae19-e204-33e0-9135-d8447f3a2471 | -11.33346 | -58.92048 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fa12e8b-64a9-3576-9e1e-8c196373fdd8 | -11.12667 | -59.09085 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60c832fa-a17f-31cc-af05-48ca2a680629 | -11.12603 | -59.09473 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ae7a6d7-afba-3c50-86f3-d3a391663cab | -11.67447 | -59.89972 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0e6d21a-693c-3a50-95c9-798711c1b195 | -11.67023 | -59.90321 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1d70628-8726-311d-8b19-7e26aee98244 | -11.66955 | -59.90731 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97dc0f30-d545-3491-a71a-94e8113f741e | -11.57646 | -59.99063 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076dd79d-0fd8-3923-8fc3-063842db0706 | -11.57498 | -59.98892 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b3230e8-a38c-38af-93a4-157611557b8e | -11.57287 | -59.99003 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3469e6f-5672-35b7-901b-a661c0ac31ba | -13.65887 | -60.15737 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35644295-12cc-345f-99e3-6b67023f0885 | -13.24371 | -59.82344 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d999eb9-aa1a-3196-b575-d8056dd7dd7c | -13.15279 | -60.42182 | 2024-10-09 05:04:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ca7ab54-ce86-3741-9bac-b832676c77a0 | -13.15228 | -59.69844 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b764824a-2582-335c-8c45-86dc5d2433a9 | -13.15122 | -59.69587 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 834c02fd-c4a7-35d6-b046-d1e387b9fe0c | -13.15057 | -59.69979 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c1b20ea-4b22-3d02-b16e-a05510ed32e2 | -13.1488 | -59.69786 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 653dadf8-07fc-3948-8286-14ebffe0df51 | -13.12692 | -60.14881 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f7ea916-c877-34a6-99e8-b490e07c59d8 | -13.11146 | -60.15391 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40219226-7214-3d58-889a-d6da944963d6 | -13.10792 | -60.15328 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d440819-f1b7-3a80-9487-0e81c3b4164e | -13.10723 | -60.15738 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c56f55-4b99-3859-91fc-62bc48a25061 | -12.97022 | -60.08969 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31f5e7ad-dd85-3c7f-a77f-b0681d1d23bc | -12.96954 | -60.0938 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e44c4ec-1080-3df4-bcc1-3a858803e1cd | -12.96668 | -60.08905 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9731264c-fcbf-36fe-88e9-b75e82c43b26 | -12.966 | -60.09317 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f73babae-42a0-3478-a63d-39fc0cc9b966 | -12.70249 | -59.7355 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b99df9e-0d11-3a55-bd58-0722eedff922 | -12.66611 | -59.80307 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 747d12d9-e9f9-3523-9fb3-e99f2ddea577 | -12.66567 | -59.8275 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5c927ba-f940-3f7f-a582-a84975ca8d6f | -12.66217 | -59.8268 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e907375f-003d-3d49-9188-99fafcbd3ca8 | -12.65976 | -59.79787 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04cd560a-1cc3-3333-a675-bcb2263a4a57 | -12.65625 | -59.79727 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3fbfca6-79a7-31b8-b7ea-7f8e345d398c | -12.65584 | -59.82145 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb71ef69-50b7-3e21-8540-ec598d0da249 | -12.64882 | -59.8202 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99666c61-de5d-36fc-9f64-bb5c1da60eaf | -12.64531 | -59.81962 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 731c320e-d3c7-3598-af25-afc1301c808d | -12.36002 | -59.29314 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f37466e-bad5-34da-8390-7bb8ea9d714b | -12.35938 | -59.29695 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81c315eb-df18-3e4d-80c8-7dbade2fb9b1 | -12.3485 | -59.24059 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b221a2e-1a4b-367d-906b-acb6b7e8efe8 | -12.33756 | -59.19938 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 918aa718-7e9a-336b-9ae8-1442623c4f4e | -14.17276 | -60.25124 | 2024-10-09 05:04:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ebf75ec-b322-3d34-9a76-799ce03062f2 | -14.74377 | -60.03097 | 2024-10-09 05:04:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b686f77-5f39-3c33-a4e4-8d0d8d735860 | -14.74311 | -60.0349 | 2024-10-09 05:04:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a18e43e4-221b-30b3-8deb-9366022ef2d7 | -14.56926 | -59.75299 | 2024-10-09 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29ec856a-7c2b-3cfe-a2f5-326dfd996cea | -13.90809 | -60.22903 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 004339ac-75cd-39f0-91f0-b453758363f6 | -7.46302 | -60.50964 | 2024-10-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75c0c924-bcd8-3a9b-ba98-2695bca66c0f | -9.09257 | -61.12922 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958e10c5-ddf2-3f51-b29c-92820b6c8849 | -9.33712 | -60.31749 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 587ccb36-ec77-3585-9fdc-9fe27286228e | -9.33337 | -60.31685 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7efb2f1-97b7-3ef5-9a3b-1c9869d39ccc | -9.33037 | -60.31166 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3a510e-5904-3732-97f4-176b8717f6fe | -9.32962 | -60.3162 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67a9c024-87ac-326b-a476-a81cbb151d5f | -9.30255 | -60.33974 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d4e37e3-8ae7-381c-93cc-fb2cf8e19cf5 | -9.24128 | -60.49604 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83c0d2d5-553c-30db-ac77-c6b2b121861e | -9.24102 | -60.42886 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 916b64db-9254-3a8e-a2af-e54ca98e01df | -9.24023 | -60.43351 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d33ad7-d751-3857-863d-0efe6e55f795 | -9.24005 | -60.45746 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 476403b1-7f83-3ebb-856a-3456bad191ed | -9.23924 | -60.46217 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f11cfe01-c0a7-34f6-a222-ef4ac90e8b67 | -9.12195 | -60.39854 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f057f34a-93a8-3416-8a3e-ed544d2c5898 | -9.12142 | -60.40071 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfb0d0df-4ae6-3111-8e8b-78f4f5013d21 | -9.12119 | -60.40316 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd2e88c8-5182-3906-87dc-41aef567c33e | -9.12062 | -60.40535 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df94c86-b765-373e-8fef-f71b51c723de | -9.09502 | -60.53842 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4725c9ce-88a1-367e-9423-e1965ffaa614 | -9.09439 | -60.53563 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed587d23-8e95-30ce-a5ce-2576f9e3d530 | -9.05759 | -60.55137 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb8cf52a-07e1-3407-8ea1-919e6032b08a | -9.05057 | -60.45322 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59cfaa62-1994-3f20-9bd3-16e1691b6eeb | -9.04979 | -60.45787 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d51fd326-1a11-39ab-a6de-ab3822c4074d | -9.04679 | -60.4525 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README179.md)
