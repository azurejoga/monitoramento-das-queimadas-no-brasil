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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32b881cc-8c30-3d26-8ead-d3781c004dd4 | -10.47782 | -58.76557 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b2d9322-027c-381a-aca0-0cef3ce4376b | -10.47705 | -58.77002 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a5f6916-b738-3ac3-ae2f-dbc17befb467 | -10.47531 | -58.76249 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22d02418-e2bf-309e-a596-5f3dd0d3d104 | -10.47486 | -58.76073 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb570289-a9c3-3d59-9dc8-d048d00e1048 | -10.47411 | -58.76509 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78176530-32e2-3ff6-a8a1-67b295babc38 | -10.47231 | -58.75776 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2146ebab-3151-38b6-8b77-f1099fc3ee33 | -10.4716 | -58.76203 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dba2fd1a-b140-363d-b777-1bab58905b78 | -10.47114 | -58.76029 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34beb6ab-66e7-34f7-b09e-c9b76e9d03c2 | -10.4686 | -58.75732 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fd3bba2e-606d-3bc3-99de-8b8b66a5de20 | -10.46788 | -58.76166 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 517ed595-0a8a-3d7f-951d-8d08a4d6b6b8 | -10.46489 | -58.75691 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41db8c99-bc58-3819-a269-6b92ccd23c8f | -10.46416 | -58.76131 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d04c37-6fdc-3213-bef7-eac1a7c57ea3 | -10.3535 | -58.89854 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64aac8fb-ba9f-3b75-a3d7-1b14cdffb9b6 | -10.33173 | -59.02529 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b30e8a3-8762-381a-aae5-c2a1ddd81841 | -10.30243 | -59.07913 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d245d8fc-7204-3fd6-822d-721f96ce358f | -10.29869 | -59.0784 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef26aaf6-00ba-38e1-9c18-d758b05953db | -10.29675 | -58.99785 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99f32eee-a2d0-3179-8d0f-b92619600ff0 | -10.29378 | -58.99266 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8e1ca2c-8e54-3e83-8c9e-75e0ae7ae2da | -10.29302 | -58.99719 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b6df369-5b4f-3b94-a77f-16329b7f9ba9 | -10.22057 | -59.40363 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9027db76-44b6-386d-93cc-ba740fd3de4c | -12.15198 | -59.71401 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 505a4248-d55e-3a02-9c06-e9a2fb45bd1e | -12.14505 | -59.88441 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83e91a8b-b514-39eb-b991-e51edb05520b | -12.14251 | -59.7467 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdb4deee-ebac-3a5a-8690-6b7dc220f179 | -11.58528 | -59.98975 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 592cd200-7dc1-31a6-a63e-801a5e312fc3 | -11.58226 | -59.98415 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01fdebf4-638d-39b8-89d1-d781921e083b | -11.58174 | -59.98205 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa09065e-7562-3dfc-b997-b75b17bd9b19 | -11.5814 | -59.98904 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d86dd2-fcaa-3837-811e-e615ba671f17 | -11.58092 | -59.98689 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fd248ef-f3e2-323f-b724-0f92c830e823 | -11.5805 | -59.99413 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 551b7c02-a678-3e53-9af0-57c848d4911d | -11.57837 | -59.98347 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1aafca5b-00f0-3942-8506-2751fef95917 | -11.57533 | -59.97799 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6690b39d-ecc2-34cd-b853-9868d2d57ee6 | -11.57448 | -59.98285 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7242f896-ff63-3f80-b61a-0655f3ce1331 | -11.57396 | -59.98073 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b66bf566-4838-33ee-b38e-83240c13f438 | -11.57058 | -59.98222 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9129122-4231-39e5-b4c8-88eca18c030d | -11.56971 | -59.98711 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb754344-0858-3fbb-b564-028f234f11b3 | -11.56882 | -59.99218 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7626404-9ad2-3c8b-8c29-e41e049cfa63 | -11.56838 | -59.98999 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e78e5b25-955d-3139-98e5-c333623861b2 | -11.56752 | -59.99507 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed604e4b-0e99-342c-a63e-ecd646ce26c9 | -11.46672 | -58.98584 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9102efb-e2bc-30b5-97ff-56564a21cf56 | -11.38461 | -59.19792 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb98f6ab-c8c8-3653-b79a-2e5ad0b064f6 | -11.38275 | -59.19947 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92016043-844e-35da-a3b1-a74601c211a8 | -11.38089 | -59.19722 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e403e3f-7e23-34eb-a8e2-3d82911411ba | -11.37903 | -59.19879 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df30dcbb-c96e-312b-b2ac-6e0636465b8f | -11.37717 | -59.19659 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58347bd0-26a6-361a-a9be-309592f065a2 | -11.3429 | -58.98412 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7994f819-e78e-3e2f-8a3b-0a9f85e7f789 | -11.04041 | -58.97385 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3da2783-8f86-38cd-a00c-48fbac87ecd5 | -11.03672 | -58.97321 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564c05fc-02c2-317d-9094-cc9e913bb4a3 | -10.99729 | -59.00348 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4995441d-e2b3-381b-aa0d-89d4510cbd8e | -10.99652 | -59.00797 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 422d38c5-c0d0-3d3b-a434-b7836258a655 | -10.99574 | -59.01246 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 277b3f1f-be48-312f-ac50-a48ffab15645 | -10.99498 | -59.01692 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3903622c-0231-30c0-ab68-32c1483516b1 | -12.31875 | -59.25966 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcb7d1ad-245a-34c6-b52e-b5162c5afa57 | -12.31212 | -59.25401 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eacb10f-9a60-37ed-85bf-a71e0ba02b11 | -12.30074 | -59.16518 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c78844f-f690-36bd-aacc-68592a301e13 | -12.29998 | -59.1696 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 169fa586-e13c-3162-a736-617ebd9db024 | -12.274 | -59.21062 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0edc63d5-5b61-32ef-9e1a-432430451b2c | -12.27031 | -59.21 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 158a9025-0f24-3f57-b536-8fa11b4ce68a | -12.26955 | -59.2144 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c929e5f3-c3c0-3447-84f1-ef752016bbec | -12.2688 | -59.21881 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7cec6bc-b788-349c-a869-d2b8c533bb85 | -12.11516 | -58.73523 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a117a830-b02f-301c-b95e-3e4aca9c0ff0 | -12.11419 | -58.73193 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab418c15-1f95-380e-b210-f1db4661920e | -12.11349 | -58.73614 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f32264dc-451a-3644-8c1d-e8a7cb1c690f | -12.11157 | -58.73458 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9498d81-20d9-3174-b6dc-5d3d69c0a396 | -12.107 | -58.73065 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 212443d2-ec9c-3fc0-8705-5624e5f2a22a | -11.89363 | -59.0174 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68e3063b-4569-3b0f-84a5-a95a3162e00e | -11.89146 | -59.00805 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16b29846-dcfb-327b-a846-4bf67569ccfa | -11.89072 | -59.01238 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec0031e0-e82b-30e0-b25d-1519e27f7b12 | -11.88779 | -59.00745 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c878c166-dfd4-3631-9bff-89c015aabdcf | -11.88638 | -58.99368 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6400e1-9613-3950-9b8a-6b05a8c66e39 | -11.88562 | -58.99806 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed40d94d-1888-377b-8087-2021afb620fb | -11.88488 | -59.00242 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91181d5a-c9f7-3090-810d-69058b6b9982 | -11.88414 | -59.00676 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c69d6565-2a03-30dc-8711-726408c88f33 | -11.88273 | -58.99297 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 513919be-d128-3fff-b36c-5bb6c95da14c | -11.88199 | -58.99731 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d8408dd-9f8b-37b4-8f1f-391d14fd830e | -11.88125 | -59.00165 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d7d111a-92a2-391d-95d6-da8db8c6788f | -11.87908 | -58.99231 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a1c945-5bed-3d61-8b86-e51d09d665a9 | -11.87834 | -58.9966 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 847de4e0-ae77-3429-bb68-544fab6396c0 | -11.87467 | -58.99603 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1beff88-cd27-3635-97df-30b0148641cf | -11.87392 | -59.00042 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12e552c8-7f71-3059-a975-93fd71923d92 | -11.87301 | -59.04975 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6c2f2ef-afbf-338f-a1a6-ddd6e52165bb | -11.87226 | -59.05415 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a35550c-978b-3b65-a61a-aeea8c18c6f3 | -11.8701 | -59.04471 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 147167e6-f5ca-36d9-a2f4-553d4d055d72 | -11.86783 | -59.05795 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeac26a6-a36f-3e56-98e6-33bb122ca4c4 | -11.86417 | -59.05727 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 130efd00-3042-32ae-91ac-beb4dc5d5a5f | -11.86133 | -58.89718 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddc0e9ef-a47b-307e-82ef-887d552a2323 | -11.85041 | -58.87292 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 670b86c6-a0e5-35d8-b14a-4ed737bad7c3 | -11.84463 | -58.88507 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e59f2bba-756d-3a8d-a49a-410df3ef062d | -11.84026 | -58.84425 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08cb1f77-a865-3c6e-abae-9c2ea78abc4b | -11.83953 | -58.84858 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f277ed7d-c874-3325-8144-461c4bfbe9c6 | -11.83737 | -58.83924 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e4fe9b25-1b7b-31cc-88a0-7db88016e930 | -11.83664 | -58.84357 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ca1d6080-fdd4-3d7b-9455-7d476209a371 | -11.83591 | -58.8479 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 64f61e15-c669-3d28-99c4-261595b2b613 | -11.83518 | -58.85221 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebd4b3e2-73d3-3201-b653-4894718c59e1 | -11.83374 | -58.8386 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| c9ebc266-49a9-3864-b87a-5528d8589eef | -11.83301 | -58.84291 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 35c527d6-d677-314a-9841-29d6ea51953d | -11.83228 | -58.84722 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cdc1defc-51ea-32bf-9604-e817c9b6f326 | -11.83156 | -58.85152 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7196737f-73d6-3491-99aa-138f7b09c457 | -11.83083 | -58.85582 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c2610cb-3172-3f79-a19d-9c7324a36c19 | -11.83011 | -58.83797 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 69577eaa-a374-3eb4-9c30-14937f5b2764 | -11.82938 | -58.84226 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README79.md)
