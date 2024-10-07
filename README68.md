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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 458bfb3c-5ff6-3497-a7bb-ef2c082691da | -20.44014 | -47.69767 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 416584fa-d708-343f-aee8-6ef4af6eda71 | -20.43923 | -47.70263 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e7dae45d-3241-38b6-abd3-d11f5939f5ff | -20.43739 | -47.71278 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 4cde21de-7c14-31fa-95ee-55299cf04ebc | -20.43722 | -47.69187 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4213ee8b-f92b-38b9-8d13-314ae86dff4f | -20.4363 | -47.69695 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1c0d2f18-93b8-36ae-8251-13dec573dac4 | -20.43539 | -47.70191 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 660dfb42-dc7b-36cd-a0f6-0636bdf89619 | -20.43448 | -47.70695 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c9646a12-af9e-3d9d-87b5-1fba2a8d5ec8 | -20.43355 | -47.71204 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 804cdedc-8828-3d0e-9b8e-89c4658676b6 | -20.43156 | -47.70117 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15f62f31-b1ca-3153-952a-5b37298e21a0 | -20.43064 | -47.7062 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3101f039-6a01-3c9a-b5f9-1dceac2c0692 | -20.4268 | -47.70549 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef427ebb-28f7-33a3-b7e5-1aefc08020a4 | -19.80152 | -48.03003 | 2024-10-07 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5b866b4-6750-3e20-bd7d-c79fd82dbdae | -21.85471 | -48.44254 | 2024-10-07 04:04:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a625f54-89dc-3de7-88b4-80c3e7a5616d | -21.85436 | -48.44585 | 2024-10-07 04:04:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02f9a2a3-5c8a-38da-bc65-d8fa95c011e2 | -21.8508 | -48.44175 | 2024-10-07 04:04:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19261dc2-7c70-35d2-b6c3-14caf3acc8ba | -21.85046 | -48.44505 | 2024-10-07 04:04:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 748352b6-3ba8-379c-b9fb-e2b2a561af02 | -21.84978 | -48.44709 | 2024-10-07 04:04:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95c98f53-61f3-3d39-9c05-e12a772fcf61 | -21.84947 | -48.45043 | 2024-10-07 04:04:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a3e6d32-55b9-3b75-ba48-9a00110aaebc | -21.65487 | -47.72346 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e72cae77-5107-3c38-bff1-e077a544d07d | -21.65308 | -47.73338 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 625740c8-e02c-3325-96fc-dff632cf5e2f | -21.64738 | -47.72174 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e888e368-6fb9-3531-b1aa-a2c3c9582230 | -21.64649 | -47.72665 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a50d692-37a6-352d-957e-b39cab4b8e9f | -21.64272 | -47.72587 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9261476f-dc3c-3817-922a-e9d4704d8767 | -21.60223 | -47.71234 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f720b353-3931-31ca-9b07-5761d67303b2 | -21.59763 | -47.71614 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d621c977-b765-3480-a7f2-88234f730d4c | -21.59628 | -47.95972 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b73128c6-5c99-3603-9900-adb93918a712 | -21.59155 | -47.96396 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| facf4fcc-3b1f-3de5-b67d-f7ec14dbd2a8 | -21.59017 | -47.71419 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01739ff7-935f-301c-b73a-d6d3caa7b6ed | -21.58835 | -47.72406 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 463a68d4-dcee-3928-af27-e92f93c97ebf | -21.58578 | -47.9522 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63a108bd-f4ac-3510-bc31-bff8fdfffd89 | -21.58485 | -47.95725 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10e4d1cf-7309-3dce-9d55-9ba5087d4fee | -21.58365 | -47.72836 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 341fb233-cb29-3663-af20-49c904a1e7a6 | -21.58087 | -47.72223 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48a64c66-aa2f-3d85-85ef-56e54fe44eb4 | -21.57991 | -47.72743 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0cc364b-ee1e-3294-86bb-d99ac1f750a1 | -21.57802 | -47.73769 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c72e0ecf-3e5d-3ee2-8be9-16e66deb3bdb | -21.57242 | -47.72564 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bd8b997-3c4b-3847-a025-f64708ef3899 | -21.5724 | -47.93884 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dfd413f-d749-3854-a9bc-25ffa11e1439 | -21.57146 | -47.73081 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8535fd88-c6ca-383a-95d4-b8fb0cf0b7a7 | -21.57049 | -47.73609 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26d751ce-ceb8-32ac-a7d6-10118f7ad8cc | -21.56865 | -47.72491 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ec6f6fc-e41f-3a84-9004-712461c0135b | -21.56768 | -47.75122 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 913f4a8b-fc79-3059-a366-e951e6850726 | -21.56484 | -47.74545 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b1c6d63-e510-38bb-9c3f-6ad321ba5107 | -21.5639 | -47.72939 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 946032b7-2bc4-39a7-92aa-6084c445cdef | -21.56013 | -47.72865 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee6d2405-6e42-37b8-b12e-8c6ba57fcd86 | -21.55709 | -47.72543 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4419df44-f1c1-3152-bd28-45dbaf885e3d | -21.5562 | -47.7304 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83fcaab5-dfc5-3d5e-8f3e-7cbf31f3fde1 | -21.5545 | -47.73787 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d0354f7-7e46-3f2c-92f7-2bb3d8e69ed2 | -21.66522 | -47.73105 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e3df49-8d0d-33b4-b0e3-da02b907be6f | -21.6647 | -47.73207 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f97e5254-ac38-38c9-9d80-ea643d2c8435 | -21.65862 | -47.72434 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33c5a87d-6fd6-3107-b80a-a0ae0ffef5d9 | -21.65773 | -47.72931 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfc91a76-4dcf-3bbe-a5f6-c382e9df37ef | -21.65683 | -47.73425 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d05efe5-8538-3b26-8493-deba517cc485 | -21.65629 | -47.73528 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062e9740-a79b-380a-9ca8-887bf102e031 | -21.65595 | -47.73914 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d827077-bec7-3748-acdd-24b409a093c5 | -21.65398 | -47.72842 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf414869-b835-3566-89fa-523f7dd14ac0 | -21.65347 | -47.72946 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 494bcb1a-bc80-3361-8390-7be28b7f356e | -21.64361 | -47.72094 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9744cab7-83ae-3f5a-a89b-ee68f3925965 | -21.63608 | -47.71945 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7adc5251-d3b7-3c20-828a-b3a795ce7d17 | -21.6174 | -47.73624 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5b4404a-f503-360c-9281-c83bb133aa02 | -21.60418 | -47.72305 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 857218fa-428b-3a6a-a1bf-50fd7562997a | -21.60134 | -47.71719 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d14aba5-9fdd-3496-bf9b-5312fdea89c5 | -21.59851 | -47.71133 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dad95f82-6fe2-3aa7-80ba-072db2dbfab4 | -21.59721 | -47.95467 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 108bb42c-5f19-3a4e-81c9-591545efa9c1 | -21.59616 | -47.93872 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 067d6a95-7995-3ece-8f0d-62a37ed472c8 | -21.5949 | -47.73099 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 49c3d633-f004-323e-a443-3c5545c9d16e | -21.59478 | -47.71037 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67234245-efaf-3bf7-8b7f-4a6988d38b48 | -21.59339 | -47.95387 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 649093f7-fb3c-3d4c-b6e7-25e886497a71 | -21.59247 | -47.95891 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5dfd8b8c-acfb-33c3-ac74-5ef999e8ba1a | -21.58866 | -47.95809 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 469a5643-39a0-3c8c-b4ae-751250bb0a5c | -21.58855 | -47.93711 | 2024-10-07 04:04:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d4cf138-7340-399b-84c7-fff11f0ef740 | -21.58739 | -47.72926 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 47f65152-789f-3c6a-aa48-e00b4a451b1b | -21.58554 | -47.7181 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 240c2a9a-a26a-3d0e-a6a1-14b992c913d0 | -21.58462 | -47.72313 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 002673b2-bf29-3070-9a29-f4a07bd96f8b | -21.58382 | -47.94133 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4ce4572-73f1-3d6e-a263-7ae7317fa325 | -21.57993 | -47.74854 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 78b1f0ef-26ee-3502-99ac-fea61d828f8f | -21.57713 | -47.93467 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 639a047a-2101-3784-9a2e-54ede08e3750 | -21.57709 | -47.74273 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 110cb61a-20c7-39c4-a124-1c9867fc20ec | -21.57617 | -47.72652 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c3551c9-43cf-3851-9c49-5f140688659a | -21.57523 | -47.7528 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 96230749-4e1b-3333-a508-c6249262a360 | -21.57521 | -47.7317 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c901e63f-a70a-36b7-b81b-8f68fe44afff | -21.57336 | -47.72054 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55ec8fc-4013-3678-9a53-13966677447a | -21.57332 | -47.93385 | 2024-10-07 04:04:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dd473f4-8472-3ce7-89bf-d9b85714ca92 | -21.56672 | -47.73528 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1650493-ae28-3ec9-aa12-9811ac2d4b13 | -21.56585 | -47.7611 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9e36765-a7e4-307a-bdb8-1b186fc54acf | -21.56392 | -47.75042 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddb84266-e4b7-3db3-be39-3dce4388e531 | -21.563 | -47.75536 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f08309fe-ae43-39fc-8026-5efcaa7cb318 | -21.56199 | -47.71865 | 2024-10-07 04:04:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 057433a1-b9d5-3bd5-a8f2-606725e3a2f4 | -21.35431 | -47.6608 | 2024-10-07 04:04:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e40c517a-5e15-37b1-bb2e-c5768fd503e2 | -21.32163 | -47.60524 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ef9c5391-bdf9-3aa2-9df2-c7ff8b3d2999 | -21.32071 | -47.6103 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 48bb7275-5136-3bfb-94fa-4380cb9ab0f4 | -21.31791 | -47.60424 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9c5f4d23-7c56-3d5e-9a4d-b5224f846c00 | -21.31698 | -47.60937 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 565ea78d-1557-3e05-9d4e-3c9bf232099b | -21.3142 | -47.60324 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5020f055-f855-31f2-958f-ddb2a6dc24d6 | -21.31326 | -47.60839 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8dba1ca7-8be3-3f48-be4b-c76410f43c87 | -21.31231 | -47.61363 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84e281f6-5246-3fd9-b60f-bf374d3dbd8e | -21.31046 | -47.60234 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bad50443-2159-3ab5-bace-4a58eaefc338 | -21.30953 | -47.60745 | 2024-10-07 04:04:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51b26cc7-d55b-3fd4-a91d-ef56905f8213 | -21.28676 | -47.39305 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 803e42c9-e196-38a6-af0e-bf7fd4f73a60 | -21.28612 | -47.39066 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44e0d55d-3494-3b72-bce4-1fb4e54451a4 | -21.28525 | -47.39553 | 2024-10-07 04:04:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README69.md)
