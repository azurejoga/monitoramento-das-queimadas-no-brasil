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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c8a278-12c9-34b3-99eb-cdb143cc5e33 | -3.60251 | -49.99158 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 82a40830-de53-3085-b7e5-a7fa74269d28 | -2.61523 | -54.21585 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25139620-6b32-32cb-91fe-815477db5dd1 | -1.06518 | -53.2248 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fd46d4fb-6b1f-31e7-b7ee-c14b4e5e6156 | -2.11648 | -50.34074 | 2024-11-30 05:27:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eb5cf54-c44f-3733-8023-877c330b729f | -2.57048 | -51.83749 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57a775c8-1017-3c48-b4c1-09d456e76482 | -1.72614 | -52.48772 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8007fcb4-7024-3b12-8a38-d843ea2f177a | -2.75595 | -54.12088 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8ab500b-d92a-3937-833c-210247848bd7 | -3.14785 | -53.82396 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bbcfbbe-a247-3200-aa8f-abab2ae9bb70 | -1.69739 | -52.64215 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a827de12-e1fb-350b-bbed-0697b9124a18 | -3.30033 | -50.76286 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d45e2b6-f585-3e52-9c3f-c6a0a4e5be74 | -1.34369 | -54.9802 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8c08f7d-54e1-3433-a66d-e9a903f82d09 | -2.84177 | -54.0769 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 985f8534-7924-3c30-91b7-6d45c04fdb83 | -1.24023 | -51.79847 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3df8d34-6e45-32cc-b61a-aa86b282e3da | -2.27085 | -53.46974 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ed3ec3d-f2d1-3d81-a2dd-366c766afc8f | -1.50962 | -52.56561 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eecc92c8-83d4-3da5-a8cf-dc57c670a279 | -2.65716 | -48.79495 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70d7aeaf-fa9d-3ef9-8d15-04201d9c4d32 | 1.19808 | -55.9475 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e760163-5f47-3df0-a28d-2418f6382329 | -3.29034 | -53.28024 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e050faba-031c-3d5f-b6df-2ead7abe7a13 | -3.2964 | -50.37513 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfd8ea26-cf17-3769-a3c2-40f518c9d5fd | -2.57929 | -54.3634 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15c66cf0-5de0-3f44-9af1-3422b59519b8 | -3.11744 | -53.27522 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ee05bfd-c0a2-3ba5-8893-45c1c21c2ce7 | -3.11685 | -53.10775 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bc5c1e3-3583-3e09-93bf-d755700e228e | -3.6032 | -49.98688 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f88a911f-8ecd-3a8e-860d-01c5390ace3f | -1.53652 | -51.62138 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd55b9db-63f9-3947-b50b-6736d80f7eae | -3.35571 | -49.76094 | 2024-11-30 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8d73cd86-d0c3-37e3-b275-2a723ebbcc0c | -3.96198 | -48.09758 | 2024-11-30 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4aa82a0-0079-31a9-b283-affc39ef4369 | -2.90239 | -54.18012 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b57047bc-ed35-366c-892c-23f4884e29bd | -3.25426 | -53.86395 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fbb3f3d-c8fd-3931-a8cc-149cdad0b3d8 | -1.26923 | -54.55865 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c429c818-498a-35a4-9948-ee967c7cf858 | -3.49837 | -53.80328 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eed06614-8935-326b-b6d4-2a142ddd8afb | -2.35844 | -55.87431 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73b125d0-6782-30dc-b4fd-c93877f4cea6 | -1.43658 | -55.24736 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7626640-fc52-37f4-a62a-c97b1bb11317 | -3.40511 | -53.03064 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d129b37a-1e19-3488-bf8b-f2ed108e359e | -3.49703 | -53.84451 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5d20e0-dc11-3bf5-8143-ccbd702eece2 | -1.59579 | -52.29142 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51147cab-a640-3346-9cb0-af7cb7308d25 | -3.38409 | -50.11519 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d9ea4cf-915f-3235-9d9f-ced86dc56e42 | 0.62251 | -60.26901 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 416aad57-00fe-39b1-84c7-4a2acbdbbfd4 | -2.30902 | -49.07844 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1e9fcc2-69b1-39ec-845d-8912e218b269 | 0.9874 | -50.271 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 075e1b13-c9a7-30e8-8625-c142593bc1fd | -3.27695 | -50.59341 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86a6aee7-1d22-3816-a934-1d70f9fa4b22 | -1.33756 | -54.99153 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9eff8e39-461f-3aca-b3a1-0bb41b872651 | -1.0659 | -53.22008 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c9602e84-fcec-3317-8746-f664343bbd59 | -2.58984 | -53.98294 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dce007d1-ecb6-397b-8d33-168c0e9bd2e6 | -1.62322 | -52.45885 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90689690-6ce2-3e92-afeb-6a44dc1a0974 | -1.06413 | -53.63626 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c87b51-cf25-3a76-a1cf-b07ca0a63d02 | -2.76366 | -55.33146 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781e0b52-4fb0-39c3-ae0c-0a31b21388b0 | -3.31502 | -50.02799 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c970410-f560-3013-8e5d-a5912e0018de | -1.36227 | -54.65615 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bc3ca1a-a802-33d4-8a57-d46a4c87af2e | -1.9491 | -53.33816 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85f2644d-1aab-3391-837b-bdf4e58a613b | -3.46566 | -48.93084 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f236a82-370e-353e-a8e2-de5ee1e075d9 | -2.66256 | -48.79114 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8261602c-90f8-3cec-b208-e616701dccbc | -2.97308 | -53.28588 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f49ba01-3ac6-31d3-aa4e-cd2a2e9d4905 | -1.70978 | -52.62893 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a406f04-7c34-3bcc-af2c-5c51e44ee298 | -0.87132 | -51.7242 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a87e085a-f24c-3d34-9550-ae13a839de92 | -2.95977 | -50.57532 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 31b48ac4-9d07-3b12-9794-704d16b7fb41 | -1.2565 | -54.55356 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34ce79ba-cbc4-3508-b087-985fda222db4 | -4.08155 | -54.56346 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b2c423-f072-3dd3-ac3c-b941a832299a | 0.61698 | -60.08347 | 2024-11-30 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e43236-0afa-3f54-bb2b-c8176c83c9dd | -3.3368 | -53.21199 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56553c23-dbbb-38c3-9bc8-bb3a35351252 | -3.02401 | -54.02586 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133fe0a3-4e40-33da-a794-d1d4b3ff4928 | -3.17517 | -53.6421 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8523e279-6d02-346d-a92a-b3133bfe23f1 | 0.98128 | -50.12626 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb1e067f-2558-3354-beec-25f1c8913caa | -4.00689 | -50.35361 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04c520dd-7752-39ac-bddb-190e338079e4 | -2.84325 | -54.07943 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 29da1e1a-464d-318c-90cd-262f4e3d5a45 | -2.22768 | -53.62695 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b02478ea-7fc5-3d58-8102-3f0f0fbdc164 | -2.89066 | -54.16362 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d56734f5-2408-3723-aa23-25bc01c55066 | -2.7486 | -51.66227 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea56d99b-193a-3ce8-a83f-871e5b4ac57f | -3.10684 | -53.10614 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6eade3a-9181-380e-9297-1dfda72b4445 | -2.65516 | -48.79568 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6dc0976-5419-3097-a7a6-8736ff37e978 | -3.24278 | -50.59689 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 150cd650-d495-35b8-8a41-6ad95023991e | -3.16455 | -53.23808 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51d5590a-4271-3fb1-b3c8-3aafb290cac7 | 1.46661 | -55.88942 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fb0c985-7d4c-30b8-80d5-4937c51578e7 | 1.09951 | -59.5872 | 2024-11-30 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cf1488c-5765-387c-836a-8694b65386f9 | -3.3524 | -49.76467 | 2024-11-30 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d76af583-3e73-3806-bf66-042c28777722 | -3.96132 | -50.19667 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56158529-1d1a-3658-b90d-998170001f5f | -3.33723 | -53.20908 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1485ba8c-5721-33f7-99e7-81b1c181324a | -3.10397 | -53.82035 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab39fff0-d80a-3d50-b302-a86bbaed0ae1 | 0.59568 | -60.46648 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 909bd39f-8e0a-321a-91f4-78c7d8583942 | -1.0696 | -53.632 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c65cd8fa-f9a0-3c24-a9f2-df9d19dd4f74 | -3.38765 | -54.2835 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab610d7-3de0-36e6-b1aa-0bbac16dd980 | -3.02796 | -54.03149 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c7e785c-df0c-332b-a2f6-400db6b36f33 | -3.48168 | -53.81629 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0af13155-5a23-32e7-b376-eb0ec2b54b15 | -1.03591 | -51.74118 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e0156c4-7e06-3bab-8783-90ee5ee3f3fc | -3.34278 | -50.75105 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 494bf82c-c84f-3df6-b17a-71b490531646 | -2.66374 | -48.79597 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f82eacd8-3a67-396e-9058-54e2637fb935 | -2.26693 | -53.46812 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0fd2bd37-7330-3b0e-8a69-183a6e8db41f | -1.26106 | -54.55305 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f69b0de5-a70f-3983-9ba7-7bc3087c1846 | -2.89676 | -54.15475 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4253afb1-2aab-34dd-b449-ca30166db38b | -1.06589 | -62.65295 | 2024-11-30 05:27:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4241291-3787-39d0-9981-bdae373ef1f4 | 1.87226 | -55.73759 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c92da96e-5fe5-3320-944d-cb7fa532f41a | -3.14483 | -53.84402 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09b3203f-e69d-3c7b-973c-0f2b0dc4683e | -2.27175 | -53.46892 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 549dbf35-3d75-34ae-a31e-2ef5e92017b2 | -1.44386 | -55.20073 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7159736-1eaa-37eb-85d2-2c420c5800e1 | -3.02476 | -54.02092 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf774e67-610f-31e0-944e-53a64c4cd3c1 | -2.87904 | -53.98692 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f8aa03f-7421-35ca-b372-2c8eff376c6c | -1.1927 | -51.7631 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3d45def-1c71-374c-b5d6-b7dd6aed6fe2 | -2.87361 | -53.99115 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 008b6e23-5ac2-3efb-8b4b-db525ad817f4 | -4.17424 | -48.62133 | 2024-11-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0defe465-1c86-3091-af0c-2563571b7e27 | -3.44171 | -59.29108 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 577220ed-bad4-3de7-a1d9-2289b8b299e8 | 1.20891 | -55.94079 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README131.md)
