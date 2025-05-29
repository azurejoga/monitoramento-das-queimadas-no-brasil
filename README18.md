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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 854eeaed-87be-3173-9e52-5ade15ded1c8 | -6.3348 | -43.3832 | 2025-05-29 12:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 115ae601-1f12-33b7-9b82-e8b647ffde84 | -7.5387 | -43.3651 | 2025-05-29 12:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| bde40fd9-9b5f-3bb0-bc49-6e9d45249db5 | -6.3348 | -43.3832 | 2025-05-29 12:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a8d88776-1b36-39f1-8bae-101168420960 | -12.3898 | -49.9786 | 2025-05-29 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 957aec90-c6c6-3581-b764-2e1c7c0c98bd | -12.4086 | -49.9978 | 2025-05-29 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 387.1 |
| 8edb4afe-e3af-300e-91d5-8ea87f298a5b | -6.3536 | -43.3816 | 2025-05-29 12:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 47d70136-711a-3bd9-92e3-33629a2c8035 | -6.3348 | -43.3832 | 2025-05-29 12:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 808d1b25-40d2-35fb-bdc8-d635909fa1a2 | -12.3901 | -49.9569 | 2025-05-29 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 691c4da6-9902-3d56-a17e-25fce458f836 | -13.7065 | -45.2454 | 2025-05-29 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 82cf8bfa-e7be-3987-8dcf-0681affdfe71 | -6.3348 | -43.3832 | 2025-05-29 12:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2436c569-4cee-3723-a517-5467ae4f3cd1 | -8.3973 | -47.1013 | 2025-05-29 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 262f18e7-3392-30d7-8ae2-15ddb4713ec5 | -8.4161 | -47.0995 | 2025-05-29 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 95d478b4-aa31-36c9-949f-dcf5ba6a8ceb | -13.726 | -45.2421 | 2025-05-29 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 13f748cc-b2d2-3951-91c6-7eca2e2e6343 | -7.539 | -43.3417 | 2025-05-29 13:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 6127e486-53c9-3058-8e84-355ab0d9dc98 | -7.5387 | -43.3651 | 2025-05-29 13:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 05f40e85-5827-3696-97bc-4ebcdfd0f634 | -7.5576 | -43.3632 | 2025-05-29 13:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4fb9c173-f049-3adb-bd73-ecb9fa69bc65 | -8.3973 | -47.1013 | 2025-05-29 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| c6946401-6588-3cfb-b30f-a2a18e2e7b79 | -8.4161 | -47.0995 | 2025-05-29 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 2a3c5557-3d99-3166-aa75-6112a13026f9 | -6.3348 | -43.3832 | 2025-05-29 13:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 64e6cb0e-f523-3101-a790-03f07c5d91c0 | -8.4161 | -47.0995 | 2025-05-29 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 204cfd73-98dd-3378-9d57-dfb9e7bc1fb9 | -7.5576 | -43.3632 | 2025-05-29 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e04dd355-cf31-363d-be32-52f8740af707 | -8.3973 | -47.1013 | 2025-05-29 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 69004865-0a43-316e-923a-9695c26a92dc | -13.726 | -45.2421 | 2025-05-29 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a9cca962-9a6a-386c-9e00-810b549047ca | -6.3348 | -43.3832 | 2025-05-29 13:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cfe2af7c-b38e-3192-a659-24b61e11521d | -12.3901 | -49.9569 | 2025-05-29 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 07b9d3a6-3aeb-3912-a75d-7a07112618a7 | -7.8063 | -46.222 | 2025-05-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8a6eb1f3-2e3c-3c63-965b-3c0ed73755da | -13.726 | -45.2421 | 2025-05-29 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e8357b30-b44a-3739-9707-72ec75e6bebf | -7.539 | -43.3417 | 2025-05-29 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 145a9be7-5d49-3715-b8df-6eba1965f963 | -12.3898 | -49.9786 | 2025-05-29 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 5784dda9-d86d-3d8c-b915-8b357ca809e5 | -8.3973 | -47.1013 | 2025-05-29 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 08f99615-e774-36ba-8d87-a482da9bc8c4 | -7.5579 | -43.3398 | 2025-05-29 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 23402947-85c6-3fcf-9c0f-5fa3e355a2fb | -7.5581 | -43.3163 | 2025-05-29 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 23f76528-c682-3910-aa7e-cb1f658989d3 | -8.4161 | -47.0995 | 2025-05-29 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5f5c1567-b1d1-3bf3-819d-e73e07904dce | -7.5393 | -43.3182 | 2025-05-29 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cd002485-44b8-31b3-986d-a1b8918d609e | -13.7065 | -45.2454 | 2025-05-29 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| aed7b1c2-5556-3fae-8140-e526b47491ec | -6.3536 | -43.3816 | 2025-05-29 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4d4717c0-6e1c-369d-864c-ad29b3d49c19 | -8.4161 | -47.0995 | 2025-05-29 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 540e732e-a571-364b-95ae-b3d9f13b17c5 | -8.3973 | -47.1013 | 2025-05-29 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7199c1b3-15c0-34be-a923-94560a0c33eb | -13.726 | -45.2421 | 2025-05-29 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 65b626b1-cb07-3e2a-9758-d3f27178c9c2 | -7.8063 | -46.222 | 2025-05-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e31968b9-f280-38de-b11b-73de8c7d6746 | -7.8063 | -46.222 | 2025-05-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 029bf0f3-2b80-3ad4-ae6e-e279b56e3b2e | -8.3973 | -47.1013 | 2025-05-29 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d1a60aa4-b23d-3bd4-904c-b113e1753031 | -8.4161 | -47.0995 | 2025-05-29 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| bfd33cc1-fc43-314e-95ea-054bad408ca8 | -13.726 | -45.2421 | 2025-05-29 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| bbc10cff-a84d-3f38-9871-fc755553d0fa | -8.4161 | -47.0995 | 2025-05-29 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7b1a562d-e4e2-3c8d-bae2-8462e03b63c6 | -13.726 | -45.2421 | 2025-05-29 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 76469081-27b8-3dc6-b6bc-01d725737a99 | -7.8063 | -46.222 | 2025-05-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a050b9d2-7f28-33b2-9ddf-dea789ca1592 | -13.7065 | -45.2454 | 2025-05-29 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| da304d21-933d-3874-87e4-bbe2688ab0ed | -7.8063 | -46.222 | 2025-05-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| de8c2d76-cc0a-3a3a-845c-19c10b763877 | -13.7065 | -45.2454 | 2025-05-29 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7902845d-27a7-38dc-9c74-9bfddc7cdbb6 | -7.0943 | -44.3819 | 2025-05-29 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e237dff3-2f8f-3ad3-af7b-9bf6f3541dae | -13.726 | -45.2421 | 2025-05-29 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 7f309cc9-584b-3046-a61c-3e037be66550 | -8.4161 | -47.0995 | 2025-05-29 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d6bbb73d-9955-3f5d-aba7-86bfd82a5db0 | -8.4161 | -47.0995 | 2025-05-29 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| bc60b42e-e795-3369-9d7d-a66551f4a400 | -7.8063 | -46.222 | 2025-05-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| bc13a82c-d9fe-32f3-80c2-efa9aa6520f5 | -8.3973 | -47.1013 | 2025-05-29 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 5f9cc5f5-a466-339a-9ea6-291647b2435e | -11.6656 | -48.7425 | 2025-05-29 14:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9d2d5ad9-bdbe-3b8b-afcb-471dd0eb1da5 | -8.3973 | -47.1013 | 2025-05-29 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2eb3f3ec-269a-35f3-8c09-cc0df56b32cb | -11.0469 | -50.777 | 2025-05-29 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 20e4f2d9-4822-3f4e-9c72-1fe08f3e6b97 | -3.5483 | -43.1945 | 2025-05-29 14:20:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fc7cd94d-c151-3da3-a127-d51c36842ace | -11.0469 | -50.777 | 2025-05-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4ca79ca3-fd22-3fb9-a9fe-bc23f7f5bb15 | -7.5393 | -43.3182 | 2025-05-29 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 95233aaa-a25d-3824-b3d5-a8fb26ea56bc | -7.539 | -43.3417 | 2025-05-29 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 446479f3-c7f6-3525-b99b-05ca3270ce56 | -3.5483 | -43.1945 | 2025-05-29 14:40:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b4e53016-f91a-3647-9f46-4b7179ba0768 | -8.3973 | -47.1013 | 2025-05-29 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 82b13c31-6e2c-32ce-84d2-2110f0967330 | -11.0469 | -50.777 | 2025-05-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8de52601-bec9-3a6a-817e-49c8e54ab2ba | -8.4161 | -47.0995 | 2025-05-29 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |


