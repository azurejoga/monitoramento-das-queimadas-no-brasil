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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba959a78-75f6-3936-9df8-d7a723560c47 | -2.97767 | -54.08498 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab9e4969-3de3-3805-987c-9d135f7dfec7 | -4.24675 | -47.99386 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddc41411-f7f7-3a9c-bcf1-c677ed75bb4f | -2.62746 | -53.98722 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23d95a7f-0658-3eda-bd08-8ea1fdf0c274 | -1.29924 | -51.73213 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a2f64de-b5f5-3f14-9277-22efdaff0d88 | -4.29638 | -46.9033 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c581f77b-c09e-3b8a-ad36-16d29eb98753 | -2.7398 | -54.11187 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93f0339b-ae4a-3ab5-85ca-bb87416d0ad8 | -1.17658 | -54.12769 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa9df303-b3f5-3c9d-ac23-d00436b2c358 | -0.93862 | -53.215 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a5ec55a-d811-35a9-81cb-d16bec1b001f | -1.25112 | -53.35965 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc6d9dd6-6462-3e98-8f57-457f8dca493a | -1.21455 | -51.7375 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b067cf98-aa35-36f6-8698-8f67a6d9153e | -3.50677 | -53.81925 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33369218-a850-36ba-b221-e8c25b063f9b | -3.26374 | -53.70646 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 661fd716-0ad0-3401-aba7-8845d54ed2e1 | -1.70978 | -52.48763 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e30a1ca-d299-32dc-8ccb-0b5d1b1e32f4 | -1.09951 | -53.61222 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e76923-00fa-3a27-aba8-a6c9180cadd9 | -0.98187 | -51.70919 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70fdf60c-3eda-3dc7-ac24-3f1f2398a1a1 | -2.80001 | -54.11405 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9abc9c7-59fa-3490-bc9a-648fc5e9b942 | -2.79266 | -53.00397 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8bcfd0c-f800-3f7e-b2f8-952e8d959130 | -3.6541 | -50.2345 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a74eb1b2-a913-30a3-a4bc-deb3395702e7 | -3.7408 | -54.07594 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0b3079-e633-3107-8ce0-cd0f4fbdea90 | -1.72248 | -52.49015 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f8dc20d-4059-34e6-8d99-510acc77399e | -1.76356 | -52.7055 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28aaf015-82ca-3588-b05a-53a237ec2700 | -3.96034 | -49.87814 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d73af4b-bb1c-3d96-b7f9-b1589b86cb65 | -3.8252 | -52.23626 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a124623-96a2-33c3-8c9e-37cce789c5e5 | -2.78747 | -51.41072 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6922d210-eb04-30cb-9064-a66aa84df8c8 | -0.33685 | -51.53711 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f1acc3d-3c2d-39db-977b-28a5c8381dea | -2.97 | -53.85221 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e67b90-1b21-3da7-a092-b3ce7d61320d | -0.82077 | -51.48756 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29073163-0c96-3735-8f01-ad53c6c6d089 | -3.01571 | -54.05518 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb235b76-7869-3c92-b2ac-b956f067c9a5 | -1.19838 | -51.77486 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a1f1b04-11d2-383e-8009-0d28d4a129c0 | -2.60885 | -54.25701 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca27c07-0dbf-3baa-92d0-99fb269ba084 | -3.31709 | -54.0947 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4a6c465-c129-30f6-b44e-fa14c9fb635e | -2.90192 | -51.57156 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99e07342-f2ab-3b89-a544-dcaf6f4161ea | -1.05077 | -53.66151 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d61ecaea-efb3-3b40-b395-d4fbabfff620 | -3.71418 | -51.77941 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6a12375-3579-3d90-8665-08f4d100f7d9 | -3.22424 | -53.93809 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0567aa6-f4a5-3702-9760-8e436f3b0266 | -3.84915 | -52.14849 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43cdfef0-bf32-310e-a524-4f1401894b6e | -2.31803 | -53.60784 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a3d433c-795d-32cf-8bbf-215629f9dcd2 | -3.90833 | -52.25644 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fada881e-cfc8-37bd-bf05-2eac87169ee5 | -3.05086 | -52.76051 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b037c37e-951b-382a-8c38-86aa2d935243 | -2.75643 | -54.07149 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc0c155-41c8-3e5f-a783-7241f904fb6a | -2.20676 | -46.35832 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46430e7-ce2e-3f7e-9f67-4761fda64ff8 | -3.67239 | -51.73615 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6029ef1b-6af9-3a03-834c-fd2c2a1e0de2 | -1.24816 | -51.74271 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26b1a771-5956-3b99-95c9-0373c82f0b6c | -3.63476 | -51.14833 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3935b3ba-b56f-31d7-acf1-9d21c4bc8365 | -2.85378 | -53.99022 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66a4ed3a-8649-3bcb-95fc-39921340ca6f | -0.82034 | -51.60055 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab0f53fd-60ec-362e-8c4f-d494290fd56b | -3.15628 | -50.587 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fc3fee8-9bf3-3016-a106-3e2bc3f0060f | -3.05577 | -53.22191 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9f906f8-0ef5-34cd-a1f4-c6a6fbc4105b | -2.31286 | -52.1743 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00939b9a-a293-3ab6-8f29-4b1c0257aa91 | -1.13179 | -53.81414 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba87b35-706c-309e-b6c0-1154abffa594 | -2.0115 | -51.17381 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94a650bd-99f8-3ece-aac2-7a412e5d07b5 | -4.23782 | -48.67008 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3249dda8-207d-387d-aa0f-1c65cc20fdf8 | -2.99633 | -53.7286 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 262e3392-79f7-3100-990d-368b737ae3a8 | -2.81438 | -54.02331 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be090b44-8ae9-3c2a-84b5-a8dc99a07ac7 | -0.27687 | -51.50242 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98a2d2d0-42df-3897-8389-c8565cac4624 | -2.0275 | -51.18387 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed7f5afe-ce11-3ba2-b530-b295b95a128d | -1.13265 | -51.67775 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c840e62f-d650-3778-92b8-8836233e2deb | -2.70412 | -51.99144 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56a6a83-a38d-3d48-9b2c-1bf2548bfe22 | -2.40658 | -53.84181 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20993f2e-9c6d-3430-bca5-d6da893b2cdc | -1.25714 | -51.75136 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68e53f50-aa75-31db-8414-8bd4467cc8fd | -1.48789 | -52.52073 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f96917e2-77df-3dc4-9c82-5e73e2cdfee6 | -1.44503 | -52.44675 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7daffe49-1d56-3257-92ce-4fcdd276968f | -1.19824 | -51.97315 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f777c5-3691-3996-9be0-a7f760c48d3b | -3.2878 | -53.83422 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b304be71-b83b-30ad-894b-da7987c5d9e9 | -1.11334 | -53.3942 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4760f06d-873d-3f4f-a596-7b75e0a519d0 | -2.17287 | -52.08027 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d36dd5-4d16-327a-b1ca-6c602e4ce9ac | -3.51451 | -53.81338 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1177548-b4d2-3532-9ee8-a65c0c291abf | -1.19277 | -51.76675 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f0a156d-de86-3b4c-90e7-4f4522fb918e | -3.84351 | -48.94915 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b33bc4d-0d62-331e-a3dc-6fd8e8904b1e | -3.63352 | -52.25401 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bec96d64-d6bb-3fee-9586-41e6df829f76 | -3.82564 | -52.41091 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f24298b-2906-38ba-a22d-47903133ae65 | -3.28859 | -45.7367 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4c004b58-0ab8-3d98-8c47-baad527cafa8 | -3.91659 | -54.51935 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af792a8d-b128-3098-ac70-9f1c08ebc6e9 | -1.61639 | -52.22067 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5406fa5d-9ba4-3665-bf1e-8eaf98184d79 | -1.15116 | -51.69153 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a4ef0de-082b-3ec7-a217-2bf437df9a46 | -1.46584 | -51.15544 | 2024-11-25 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 032a60c8-e1c1-3172-a475-15b18c3cbde9 | -3.23566 | -53.62782 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06b4e30-c1af-3a3c-9c2d-806d540ee788 | -3.12467 | -54.17932 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49c56be3-8207-3271-a5f0-821d6ec6326c | -1.24761 | -51.74625 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41c55b21-c5ea-3c40-8b22-5c1bb2f2014b | -3.94761 | -46.89576 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30a37cb2-05e5-39aa-8b6c-6ec3b3965397 | -0.97796 | -51.71221 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aedbfcba-651c-3f18-afae-a02d1cf68244 | -1.15546 | -53.40493 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 096fd9c1-708a-3798-998f-605525c4c934 | -1.12994 | -53.6959 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358fd2fe-e8a2-391c-bfb2-7457397573b0 | -1.30878 | -51.73724 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeda03a9-9ff1-38c3-ba51-45cebb1e9d12 | -0.95157 | -51.65023 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d8ae92b-c9fc-35fd-a820-6b433743cc1c | -4.81259 | -45.75186 | 2024-11-25 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ae4c5d0-2625-3924-ba29-213fd4dee8cf | -1.76078 | -52.70153 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eb84f14-d1b0-3a15-ac33-b13c97e85dd9 | -2.1768 | -53.77412 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e9d4417-0662-3f65-8251-ac29c87a24f3 | -2.75364 | -54.06748 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccff6350-ae0a-3cc2-a86b-04ac84f64b86 | -3.51341 | -53.8203 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6646077e-3ee5-3c33-9c61-2be34d54c3ad | -3.12123 | -53.10842 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb63530f-ca87-3da5-9a93-f7f307e0607d | -4.36933 | -48.57158 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0812a35-eaef-36ed-9228-866039587e0d | -3.25788 | -53.27095 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e69b0e2-b76f-3de7-8a23-e821e87f728d | -0.24572 | -51.61347 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42eb9a16-40f0-320a-b2a0-346e7c94e3b6 | -1.28457 | -51.66473 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ff3b9a-38c8-38da-9f2b-9fc642e303a9 | -3.578 | -54.52029 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfe5cf47-c6c4-349c-a360-82c71332b96e | -3.28115 | -53.83319 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f655806b-480e-3c48-8962-53f6c3148a05 | -1.06153 | -53.18819 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f14596b-6bfc-3942-b0d1-74b84e1860f5 | -1.77412 | -52.72482 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16885b95-3177-3b42-9fcc-caa0a1f9253b | -3.82183 | -52.23575 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README36.md)
