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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f46d294e-1d21-372f-9e94-883fbec86013 | -3.70547 | -52.42052 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49b98a24-4e0c-3435-b0a3-1180d5d98f56 | -4.29314 | -53.89635 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fece66ef-592a-3593-bf06-3425568b8c64 | -4.29259 | -53.89994 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adcdf2ff-c09d-3739-8919-3195c5d6d6ed | -4.28318 | -53.69234 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47d4e869-08c3-3f87-84ba-43530c8286f8 | -4.2798 | -53.69182 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bce7165-d38d-3410-9726-19ad921c1e92 | -4.11103 | -53.50993 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b726d9-6801-302a-b81c-897d62359bab | -4.10889 | -53.63626 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0ee2ac-b2da-326f-af37-470f2d27e0fa | -4.10763 | -53.50941 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 844ff054-e049-3cad-8bd6-7b8908f8ad06 | -4.10551 | -53.63573 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82ca255f-57f8-3d38-af16-5fd6ff44d332 | -4.10495 | -53.63935 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df04e263-887b-36a2-948f-372c1dbea6a6 | -4.10213 | -53.63521 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ccf5fee-2704-3e77-acfe-d997b8bb1835 | -4.10157 | -53.63884 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2037cd7c-86e6-3b4a-842f-fb14d1a1f5fb | -4.07776 | -53.5683 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31a93546-47e1-387e-b03f-cfa447b54749 | -2.03326 | -54.93171 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2a4e8f-c245-3f26-9d14-f3f1e8e912bc | -2.0305 | -54.92777 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a5545db-5f79-3f7c-9dcb-c82d759cf1d1 | -2.02006 | -54.92968 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c097f9d-7abc-328b-aa81-fe4b8ad36922 | -1.98022 | -54.89889 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d335172-f012-3907-8a8e-b10a99b926e5 | -1.97309 | -54.9013 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbb2a10e-5e13-3dd8-b79e-f2a9bcc2bf25 | -1.90444 | -54.59953 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ca00c2-2cf3-3911-981a-2a682eb64864 | -1.87075 | -54.68557 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c2a9a6c-6d3b-35e8-b62f-2f566576cbf7 | -1.87022 | -54.689 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 882d6b6c-05b2-3a67-9e39-3c743d88a3a5 | -1.82495 | -54.38987 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9790c6ab-f7e5-3511-af5d-2543580d3607 | -1.82165 | -54.38936 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31a6df95-4890-3251-9d01-0be217f1fa3e | -1.78903 | -54.84138 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09eab637-4e83-3c00-9eba-765f5add5637 | -1.57739 | -54.75882 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| caf0d1ff-93bb-3223-b2cd-9edd74cdfebe | -1.52501 | -54.28332 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20e20f38-4af3-3a07-a473-1ef9d90cdcb6 | -1.52447 | -54.28675 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48098cd1-4d15-3d50-8f06-4918b8ad8f64 | -1.52281 | -54.49775 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6811802f-4544-3038-a1ed-01910acfd0d7 | -1.52278 | -54.27594 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e655fa9e-4ff6-3ad3-b11b-4f46054e1e47 | -1.52224 | -54.27938 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4309965d-c4ba-372f-b604-402a54ea18c5 | -1.52171 | -54.28281 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7372f41-ce0e-36b9-b4c4-380a71ee0160 | -1.51951 | -54.49725 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f4ce87e-30c0-3c20-b835-8204a3c747f8 | -1.51947 | -54.27544 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a493007-d0b8-3829-aa7e-ac030a0581c6 | -1.51349 | -54.2921 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e6cbace-5d46-3ff6-bc68-15c604ed8235 | -1.51019 | -54.2916 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a92a52-c93c-35e9-b5fa-ef99b90d7531 | -1.45481 | -54.45169 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c03178e0-ca90-3dc7-baf1-ed32605a627b | -1.45151 | -54.45118 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23d8043e-ded5-34be-9357-873e5a022b12 | -1.43468 | -54.49427 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 175b55a8-bf11-3db7-98b5-1a3cc4825ea0 | -1.43138 | -54.49377 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afeded53-a396-3efe-a2e0-68b37890c902 | -1.42808 | -54.49326 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63530918-141b-3faf-b3f3-c459e337f482 | -1.42755 | -54.49669 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d71e8cb-6e5c-378f-a9e6-2be96ecdeb79 | -1.42479 | -54.49275 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03657505-897b-3a3c-b4a0-833454c02a04 | -1.4212 | -54.79717 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73ebad8c-6ca1-30f3-9bdb-7922122a7e52 | -1.41969 | -54.23902 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2055779-3b53-3f4d-b9b9-91cde80f0e01 | -1.41843 | -54.79324 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc0cadea-4e11-31a3-a07a-bedb3d6c6e23 | -1.4179 | -54.79667 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7adf3816-9825-3bc3-8455-2f0722a91da9 | -1.40966 | -54.54653 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31b7aa9-2a72-3769-ad12-4e257a04276c | -1.4031 | -54.21536 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 123a2b2f-8369-3b66-9b30-5674c062fb99 | -1.35482 | -54.61154 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f1a859-963f-3954-b970-b69ebc796ab7 | -1.35152 | -54.61104 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 867b9406-eddd-3d70-b629-bea8e0aaeabb | -1.35045 | -54.61789 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21a05f52-fb90-3a90-9a0a-556642e6dd48 | -1.34992 | -54.62131 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1551eca-2fbc-3bdf-be02-0b45e64987c6 | -1.34894 | -54.6492 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f72874-58cd-33c2-900f-c0df62df9f7a | -1.34769 | -54.61395 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28834bac-2ae1-37fd-8e96-1eb5601abe12 | -1.34715 | -54.61737 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c13119de-fef3-3191-8e34-90ce8cca3ce8 | -1.34458 | -54.65554 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d76af37-aa4a-338f-a2e7-707d2ea1005e | -1.34439 | -54.61345 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04fb2ebf-bbe0-3a55-911b-0d7cb03a7a53 | -1.34385 | -54.61687 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e0e357c-40fb-3673-935b-555b881f0566 | -1.34128 | -54.65504 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9414aa59-1ee2-371f-baf1-ad10612c31b6 | -1.34109 | -54.61294 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a226e16-3756-321c-ab03-2dee12adc8d8 | -1.33832 | -54.60901 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 783875ea-bd4f-3087-b12a-3f2fe8967bd8 | -1.33779 | -54.61243 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d74bf3b-b36c-3156-bb14-ead9f1d905cb | -1.33075 | -54.63589 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee89a370-3591-346b-bc12-66a468da7ff0 | -1.32746 | -54.63538 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45cec0a1-bc02-31a0-b2a4-93e518e6324f | -1.30339 | -54.22114 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4312b4e-9393-3b61-b252-4b1ffaac9c59 | -1.29847 | -54.53981 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d7d5d36-0446-3205-9b62-f3d1ebf1244b | -1.29571 | -54.53588 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc50ac5e-8ffe-384d-9119-ed40e91e9cf1 | -1.24716 | -54.1915 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d5c4c5d-99db-3a92-8f96-c9ca3f8f9263 | -1.23949 | -54.19731 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 585c6705-38a5-36d0-9573-522e9a16e755 | -1.22848 | -54.67968 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eca08696-c9cf-34c9-8901-639651e568cb | -1.21963 | -54.5416 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d94dab8d-90b6-30ef-bac3-739faf2d43db | -1.21909 | -54.54502 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f009b1e0-d49d-38de-9ff4-fba0e265d826 | -1.21696 | -54.18601 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 031abe4b-57d2-32a1-8561-6684b157de81 | -1.21474 | -54.17861 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 026e40af-0fc4-307c-bbc1-33543cff97e1 | -1.21144 | -54.17808 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6953892-895d-3c96-954c-833233558f19 | -1.21091 | -54.18151 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df351e83-b0ed-35d6-89e4-fc521a37cf21 | -1.2093 | -54.1918 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e96f49e5-a927-34c0-8269-a35ce43a2213 | -1.17075 | -54.17883 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27479e96-1492-3a0a-8dfe-b0b5cbf65913 | -1.16798 | -54.17488 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2153c7c9-1f4c-3c4b-8e28-b42f23a0551a | -1.16745 | -54.17832 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4dc06614-a98a-3f61-8940-e8549dbb0377 | -1.16414 | -54.17781 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ecdbafd9-6874-3973-9af8-a7cec2dc90c4 | -1.16254 | -54.18811 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd480d1a-9271-3297-8193-b6a0c35d46d0 | -1.15924 | -54.1876 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3a1afe7-56df-3cb2-ae3a-8628ff84607b | -2.24405 | -53.48797 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0416c0f8-1223-32bb-b5ce-43edf5ae2843 | -2.24069 | -53.48746 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e4dfc0c-0f9f-312c-a884-5ffd855f87ef | -2.1799 | -53.65939 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c6a8767-0287-34b7-8a3f-f6eb8b71a407 | -2.17936 | -53.66291 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361f624c-9139-3179-ba0c-a5d539f1ae86 | -2.17601 | -53.6624 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 913c38e9-aecd-3bdb-8390-f51e3914b8fd | -2.17556 | -53.68756 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1b4ce13-8389-3255-95ef-16133be2fe4d | -2.17385 | -53.67649 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7599677-5a39-3fcf-93eb-856f58f07443 | -2.17222 | -53.68705 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a91ce8a-1581-3546-aed0-62a6ed853bbb | -2.17168 | -53.69056 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 334c49da-4580-39ba-82a0-4c0ffea12064 | -2.17166 | -53.67278 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb77c90b-7c7c-3c21-a226-e9dfcd5d9a6c | -2.17111 | -53.67629 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa036947-fcfe-31a5-9228-09c2d7057658 | -2.17056 | -53.6798 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e802275-91c8-3e8c-9e79-cd3aa88ee1ec | -2.17001 | -53.68331 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31eb9ac7-1faa-38fc-8320-185181af04ee | -2.16946 | -53.68682 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d73d00b1-a779-3607-8618-716146ef6e4a | -2.16832 | -53.67226 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 342730cb-6f2f-3ded-90c9-ac073ab2fc5a | -2.16777 | -53.67577 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a3ff991-e35d-3124-ba70-3e76cee99403 | -2.16667 | -53.68279 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README78.md)
