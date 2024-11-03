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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42549ab3-6c4f-3128-ac14-2eb8d919b2f6 | -2.35337 | -49.10933 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73acd110-3876-3a56-9868-9b4e0ae823c9 | -2.34998 | -48.91073 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12eac65-c9d8-3558-986c-e95b9cb81a5f | -2.34827 | -48.89961 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb986f6b-c275-3308-a3e6-29dd4943df8f | -2.34718 | -48.90668 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0b116c3-bf39-3a34-83cf-6bd77e6c594e | -2.34561 | -49.11531 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e386da37-70e1-387f-9486-31fefdd25fca | -2.34174 | -49.1183 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbe36106-7d0b-3f26-b4a2-c42e3a499c84 | -2.32835 | -48.93995 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e70bc57c-b1c1-3a90-a827-76bbd792eeb3 | -2.32827 | -48.91825 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f356e95a-510b-3679-b814-bf4d10978f34 | -2.3278 | -48.94348 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df92e898-5423-3970-aa40-e5d5b89dbe6c | -2.32493 | -48.91774 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 48927e70-1fff-3654-a83c-77ff3810a8ae | -2.32392 | -48.94649 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d45e413-92f3-352b-9e02-c35b94c9aa5b | -2.32337 | -48.95002 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 141b470d-5e95-3662-8e52-520b00fe8cf7 | -2.32057 | -48.94598 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd739088-1e56-3137-a17c-18d684ac0543 | -2.31723 | -48.94547 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bd84e47-6040-3c36-b386-7ee5561d64d0 | -2.31389 | -48.94495 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41ddfd16-a613-326f-9b9c-6b8517af7cb2 | -2.31114 | -48.87906 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2039c651-ad06-34ca-b663-42ede4147520 | -2.28958 | -48.9733 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46047d89-29bc-30fd-8335-47d2b3ad8ddd | -2.27495 | -49.19747 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef104def-4e66-30a3-8792-11dff4b346de | -2.27163 | -49.19696 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 209440a0-2f22-3aa0-bdac-a0b92129abc9 | -2.84184 | -49.27048 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ef2a8e-e48f-3932-95f0-4eb22a6bc8e9 | -2.83946 | -49.37372 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6749493e-612e-364a-aa37-9d8f6203e9c0 | -2.83797 | -49.27346 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21b45f8a-360c-3bcb-9772-f266be9d7e7c | -2.82537 | -49.31087 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb0afe05-11bc-3038-b485-92a3c1e03d51 | -2.82483 | -49.31436 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b03488e6-85f6-3bb6-8ed9-d26b672ac645 | -2.82249 | -49.15266 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 70689ce1-9823-3c12-9a9e-30b82d5c7716 | -2.81915 | -49.15215 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1abfee7f-0001-302d-af67-21295f55c1e5 | -2.81601 | -49.32729 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cec2bb-a722-3f5f-99b2-b14216386035 | -2.81548 | -49.33078 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34484e8b-d74a-3ee2-9831-b624034198d6 | -2.80829 | -49.33325 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bba3b11-7f3a-34ab-9e82-ead8d91ee9f7 | -2.80559 | -49.35068 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a88caf1-66df-3bf6-ada1-56641e8128ac | -2.8055 | -49.32925 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad14dcd9-aaad-3861-b05c-9343b4961070 | -2.8037 | -49.21083 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8741bb-0f5f-37ec-9a20-08688b8e8101 | -2.80315 | -49.21433 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f6e0b3-a714-37a8-999f-60fc0f33c037 | -2.80281 | -49.34668 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4dbfdd3-c251-34e8-948c-6b1bccae302c | -2.80164 | -49.33222 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88816404-8752-33e6-82a8-989fbfb8fac2 | -2.79272 | -49.25932 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df377e78-481b-37ce-b312-5fb3a10b49a5 | -2.75015 | -49.13797 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58b4f4e0-392e-3d51-bb94-430e94a4aa42 | -2.7496 | -49.2956 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2150f807-2d47-3d77-b3ac-e68907293dbd | -2.7303 | -49.17803 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7cca167-a49d-3f2c-9fd6-9c72b03cd60e | -2.72751 | -49.17401 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98366896-d193-38b0-b979-5ee0ba55742d | -2.72364 | -49.17701 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3286ef7-7a60-3d92-8bc1-168c8f2d8bd9 | -2.71795 | -49.28002 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5afa0a30-7123-31db-a3bc-38b77ebe12e4 | -2.71741 | -49.28351 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 412f705d-a705-3c11-bbe1-f74aae63d30b | -2.71705 | -49.32987 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fd37febf-b659-338e-9ea2-4dea9d4b84db | -2.71633 | -49.29049 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddbfbfe8-98cc-3a6d-832f-6e7623fc6f77 | -2.71373 | -49.32936 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e53e7ad3-046f-3eb5-8788-78656489f377 | -2.71247 | -49.29347 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63fa9710-a708-3caa-8640-65b0e447e293 | -2.7104 | -49.32885 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d08b18b2-8b6a-3900-9956-99f7a4fa07c4 | -2.7086 | -49.29645 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33ec0c79-9062-3fce-8458-6fe7a291291b | -2.70636 | -49.28895 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bee2a64e-3046-38e4-b442-0beb3792aff4 | -2.70249 | -49.29193 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9985b4a6-1b64-33b3-b0aa-51aa58327a51 | -2.6675 | -49.2546 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4defa4cb-4de7-3427-97c3-458866ca4be4 | -2.66642 | -49.26158 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b02fe64d-28dc-36f1-9023-514e2c202002 | -2.66587 | -49.26507 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e79d1665-af1b-32dd-8b29-71659eef562d | -2.66533 | -49.26856 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86a00c6a-5d71-3771-ac5c-4d72bff94371 | -2.66472 | -49.2506 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6feeec9b-6284-3aa5-a52e-c43461c30f00 | -2.66465 | -49.40391 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8d2715a-092b-3a50-8de4-8a53dff2594c | -2.66194 | -49.24659 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df577d8c-5a44-3f55-9349-11dfe136c4e1 | -2.64786 | -49.18354 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7875e412-fa99-3cf8-b613-94f1e88966bf | -2.64732 | -49.18704 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f29c0f88-1e08-34ce-8405-9b5293025644 | -2.64678 | -49.19054 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36b4e7a8-0918-31a3-87da-4cebed30deed | -2.64344 | -49.19003 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d56c62c1-4dc6-3ee7-bc54-5c2bf3815efd | -2.63375 | -49.12035 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5311887e-f1b5-3f05-8c5a-6fd80d1f94cd | -2.63087 | -49.09473 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e117968-796b-3408-9c85-605f2f531b0e | -2.63033 | -49.09824 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f3f0899-a78c-3986-b8ee-c8b3eeeb9b5c | -3.27543 | -49.08176 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5d8f570-6653-307e-81cc-262b20c35c6f | -3.18219 | -49.09237 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424bc04d-3dad-36c4-ba4d-a46ea69ab618 | -3.1755 | -49.09135 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb0fa72-cc19-3700-94ba-f912d80b39c6 | -2.97636 | -49.10468 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a428d08f-6905-3fe2-9ce4-d9723a552fa6 | -2.97582 | -49.10821 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb460fb-7fb6-3b52-8592-80aae81bebb6 | -2.07687 | -50.33668 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e22c4be-cba4-3470-ae08-0fe802d1ecd4 | -2.07634 | -50.34011 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9df58aed-3be3-38fc-9aa0-40b090d5a976 | -2.07473 | -50.3504 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc312e8a-32f2-3aa2-abcb-d6d625f22f2e | -2.0709 | -50.35332 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| febd849f-6076-3a1a-9a4c-0b509e09e1b1 | -2.66513 | -49.83878 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e950da7c-2c2b-3092-b7a3-a90d8d78e0cb | -2.6646 | -49.84222 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b385012-5fdd-37a6-9f6e-b3b50e82fac1 | -2.6613 | -49.84171 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917e84c4-9eb8-348f-b37c-1d6260f2be5f | -2.66076 | -49.84515 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad0543b0-d95b-35c3-b1df-8c5f891b1777 | -2.65746 | -49.84464 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92d8e317-e730-363f-b195-9c4153997d5d | -2.65434 | -49.88638 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78dde099-2f4b-345e-b6a5-0953b9967ec5 | -2.65415 | -49.84414 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bee67f4-2c49-36a5-993d-0d9ac35e0f55 | -2.65157 | -49.88244 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c48712-37ff-3c53-96e5-9db7cc242542 | -2.65104 | -49.88588 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e984066d-367a-37c8-b2be-e42e86904a64 | -2.64774 | -49.88536 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87d1a5a7-9698-3d24-a70c-8146b7b95e54 | -2.64755 | -49.84312 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f72612d4-0299-3397-8d3f-82dee6b30523 | -2.64701 | -49.84655 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2058918-67ea-3e50-a9bc-7876e5c0bd02 | -2.64478 | -49.83917 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dfda1ce-f5a3-31f6-bff4-d05fa2249dd5 | -2.64443 | -49.88486 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f47285e4-8297-3857-89d4-c938f155b33e | -2.64424 | -49.84261 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f36057-d363-3ca6-bcdb-ed6bb7e4680a | -2.6439 | -49.88829 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8504757-3636-34a1-a0b0-fbae243be966 | -2.64371 | -49.84604 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df2ca51d-9ad5-3717-b151-23e488c0dd03 | -2.64113 | -49.88435 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b585494b-b2ee-3748-b6a6-a6af5b775668 | -2.62316 | -49.80416 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2002dc1-ef2b-31b4-934a-996c65f50142 | -2.60727 | -49.81932 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88d4dd78-2783-378f-8622-32249313f97b | -2.60674 | -49.82277 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 025be5d4-30f9-3e72-b8cf-97f57ed5fef6 | -2.6033 | -49.81874 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1e25a9f-8081-32ef-a758-0ce77ffae092 | -2.60053 | -49.81479 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ec1d9bf-accd-351a-96b6-3c641e729ab0 | -2.6 | -49.81823 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfbd67cd-f71b-3fda-85b5-ce8eb8c84662 | -2.5967 | -49.81772 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b5cbbc-4721-32bb-8c8e-1959f0c1212b | -2.59616 | -49.82116 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
