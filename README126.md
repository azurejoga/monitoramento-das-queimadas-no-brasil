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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2fdcbd2-6a8d-395c-acbc-d6caf4384c52 | -3.19304 | -54.3327 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d6d003-4f94-3608-924c-a433f06a98dd | -2.83873 | -52.91504 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf1bb634-344f-36f5-ba41-0b8a70b2d825 | -3.20824 | -53.8439 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 731eb113-aa3c-35b5-8ff0-f582250ac507 | -1.46325 | -54.49889 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e95633-41c6-3809-9f7f-5b2fc900486a | -2.01823 | -52.08639 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7dd0617-914e-361e-bf68-8cb700736ad6 | -3.39781 | -50.66336 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe201877-61df-3737-9b42-87023cb774f0 | 0.93654 | -50.75162 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a6cc178-239e-3757-a4bd-e907b102d362 | -2.97095 | -53.28923 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61e37b1f-eb27-35f7-8b11-727ece831d72 | -0.58037 | -51.69713 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fd1d60c3-fef5-3bf2-860d-5914f9f261c9 | -3.51602 | -62.76958 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acd726fd-283c-3a10-ab3e-152cc528d065 | -1.2001 | -51.75055 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e55804a-8309-34f8-a611-4cbfd7e50504 | -3.26414 | -50.2071 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53c024b3-d057-37ff-a93b-ca99c8968a22 | -3.22016 | -54.18521 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d425a41-743a-3237-b6b1-d7fb02930bf1 | -3.03208 | -51.53763 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9d2aae8-e4ec-3abc-acc8-a569c2a38f1b | -3.83116 | -50.14267 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5efbd3bf-505e-3e3a-9944-a008e6cc5b96 | -3.83129 | -50.13859 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04751570-2b54-30ae-861c-c208cb8a508e | -3.0479 | -48.96716 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1106bf61-1294-3ae8-bec7-45e4bcfaefd0 | -2.02452 | -52.08064 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1c5529c-3a15-334b-947d-b9cdebf486ff | -3.11249 | -53.27443 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48a5c5a3-d7b7-376e-aa8e-86b1b354ceac | -3.29233 | -53.8382 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a5fe79c-ccab-3f23-8ec1-6b267feac908 | -3.11113 | -53.8083 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b0a33f5a-ff8d-3bbd-b90f-e97441ba63fb | -3.38879 | -53.27277 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b3633b9-d0c6-386d-9813-02358cfeceb1 | -3.05106 | -54.05272 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc8c464e-093b-36eb-98d4-8476d61e0eaa | -0.58088 | -51.69385 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7c0bb5e6-2b1e-3682-b236-097bae5c8013 | -0.96868 | -51.71719 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 338c4ed6-9fc4-32ba-b2cd-4b65fbfb3216 | -3.06347 | -50.33003 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 207a6bb7-7908-361b-81f2-09c7b3831a28 | -3.09307 | -54.02826 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2418205b-890d-35fd-b9fb-0ad890d365d3 | -3.7953 | -58.97643 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d66cad5-aeb6-3304-ba4d-5a042afd89df | -2.66175 | -48.79671 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bcba2c8-b967-3ed5-8ee6-8ca4571ac0a2 | -3.09363 | -50.3462 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 209c8026-0e7f-3950-b2a2-6b0374818ac5 | -3.24925 | -53.63368 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ea89fd5-c73b-3628-9c7f-7177d37d07ed | 2.37213 | -61.26413 | 2024-11-30 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9338319b-3640-32cf-85de-854f541884bc | -1.72194 | -52.48088 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6d7f42-3693-3d6e-be0a-2a094fba9856 | -1.89282 | -54.54496 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fad627c-819c-387e-b81d-2bdc31087c2e | -1.25347 | -54.54424 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 376f3bff-4f97-378c-b62e-139c7a4c9313 | -4.201 | -50.69214 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e3dcff9-3be7-38e8-b576-957a2478a396 | -3.47148 | -50.53634 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2362107-819f-3507-9022-8d275297c195 | -1.37176 | -55.87866 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f47a8f2d-3315-3aaa-8846-b7cac26602b4 | -3.24598 | -50.59767 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 380202ce-2b5b-3719-8f8a-329a8e0e298c | -3.38598 | -50.32213 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0c5891-676e-3396-82d0-a6966c5aec20 | -2.78691 | -51.6722 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f574b79-e725-31d7-ae3e-7b977f4becd9 | -3.09441 | -53.72194 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08e0a57a-1300-3cef-8e39-a9827280de88 | -2.978 | -53.2868 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36b5009c-3f1b-33a2-b702-8e496024e757 | -2.97885 | -53.28104 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fc56bec-9a62-359d-b3df-920d6b377148 | -0.99913 | -51.73212 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10d5544c-c627-3abc-995d-baa78f9404df | 0.94757 | -50.74976 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 658dc653-8ac2-38e1-a47a-6b08054f6103 | 0.9361 | -50.74929 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2a61798-33a4-364f-b1db-99fe01eb92f7 | -1.65981 | -55.23108 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b28e6e02-9d10-3454-b551-5b8112f698ef | -1.26482 | -54.55802 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4c034e15-b74a-30b8-9e81-d79377d359e3 | -1.57712 | -53.85606 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bad5655-8477-365f-882c-434eb7ae1836 | -1.25354 | -54.54314 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36765fb7-ac55-3c01-a1cd-69ba9bdd236a | -3.14002 | -53.84358 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f25ed366-bccb-34f2-bbf3-610d283077d7 | -3.58697 | -50.3624 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82766c66-8221-35d2-b754-69f97d68f0b7 | -3.25207 | -50.61578 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33ee2284-2988-3037-a92f-fb3cdb0ffc70 | -3.08947 | -50.36154 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9ba5e0d-d572-38e5-840e-52647617b146 | -2.77938 | -54.21661 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b91d3c67-de2a-3cf3-80dd-d521ee575c5a | -3.53659 | -50.18612 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b828aa5-cbf3-38e7-8c24-76271fdc2045 | -2.96176 | -53.89331 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cebcab1d-6ad7-3876-aee6-2dbbf80c1ea8 | -3.38341 | -50.1198 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98417693-64e2-3be3-8831-fca6d1c2df0e | -1.05699 | -53.21386 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d78c36cd-1c73-3fa9-9a44-28705f0b4223 | -4.07722 | -50.03644 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| be2866c5-fa83-37ee-a7f9-128eb0ef7cea | -2.03207 | -53.49767 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4c11d43-be3f-3896-8f9f-8b23213b1f84 | -3.4665 | -48.92512 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 954eeb3e-5ea4-3e43-909e-54819cd8f375 | -1.15138 | -51.69143 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31b04eda-35d3-3336-8a5b-79e8ef0cb41e | -3.40374 | -50.66424 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 10ae7c3e-5c74-3a98-be8e-52bf30443f8e | -1.04534 | -51.74031 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f77c62f7-6dca-35a7-a191-4edbea01d4b9 | -3.24521 | -53.92408 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 27dd41c2-1243-3a45-a025-72a0c47048bb | -2.60993 | -54.28296 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e033024-a624-342e-9a21-337c96328e1a | -2.97716 | -53.29245 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64f5ab81-adfd-3c63-9e15-a9c1c82df1f5 | -3.30273 | -54.16341 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26667a0b-3e7e-31fc-b206-8a54b155c0e4 | -3.24845 | -53.63912 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6be79bdb-6fac-35f7-964e-5d92866b619a | -3.46551 | -50.53539 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d829e16-38db-3e90-bd14-6711a7435245 | -1.19906 | -51.75724 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a48a12a-4e4a-3336-97a2-50c09baf16a3 | -1.08361 | -53.63433 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d395c21-56e3-315c-addb-cd68f7bd1f03 | 1.87614 | -55.73699 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed0a7fff-11b1-3d37-bd4d-a1653ce88d67 | -2.31617 | -51.95724 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 334a0a1b-38ee-3137-b1aa-8a8a0e63aa2f | -2.5992 | -53.98434 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5af5e612-6182-32f6-8388-218c4f29cfb8 | -2.38076 | -53.68462 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a370269-60f8-3c9b-9473-cb14a906a12d | -3.51029 | -62.84942 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7aea319-975e-3a3f-9931-ce44d8a68489 | -3.27282 | -54.7006 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ba858cd-9790-363d-a17e-13d045b1653a | -4.06227 | -49.06333 | 2024-11-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76645006-d464-306e-8522-c94300ce5507 | -1.00497 | -51.72963 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1f5e827-736f-3cdf-8967-82aab195f141 | -1.50974 | -52.63196 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 653c8a57-f0b2-3dff-b202-79fc06254cc3 | -1.08556 | -53.63666 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c4ed164-87bf-347e-b6eb-4e8823445885 | -2.58516 | -53.98224 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf98765c-adbd-383f-a3e5-80e688886090 | -0.96386 | -51.71306 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e8d45c9-3c31-37f7-995f-8820f32eaa6f | -2.44819 | -53.62647 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8ba1074-a6a8-3df2-9f08-e383ba17049b | -3.96849 | -48.09356 | 2024-11-30 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63338001-c14e-3ebb-b079-92c314f483dc | -3.74888 | -49.937 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d684fd77-9ff2-3d90-9757-8cf6a4356b8e | -3.0715 | -50.32891 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 033cf4f6-998f-319f-b583-269bfe536bd9 | -1.64145 | -53.87069 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| fb3a273a-003a-354e-8efc-576e80f4ed85 | -2.60671 | -54.20977 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 385885e7-d04e-3934-be81-971f148f3dfb | -1.89352 | -54.54053 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a53da2ef-863b-30b7-80e6-adb7ed3eaa1e | -3.40004 | -53.02994 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05f4befd-3aa8-3ab0-8d0d-a634790d71b8 | -4.45849 | -56.18472 | 2024-11-30 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03d3e0c3-0d02-3cb2-a127-ed09de58d340 | -3.06278 | -50.33464 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9bc4a2e5-6376-387e-bd5c-5137d7e5e62c | -3.75828 | -49.94548 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 111326b8-8520-35b3-acda-a89f954c359a | -3.41446 | -50.16605 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a34a5a5-5967-3712-8ae0-3d6425fad814 | -1.70929 | -52.76636 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0780699e-25d7-3131-8312-5e559849b929 | -3.52555 | -62.77474 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README127.md)
