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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5b0cf7-5acb-3718-89d6-4edf4c8b6474 | -3.3452 | -50.4917 | 2024-11-22 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e283597e-0c15-3b02-8067-434ace11ffce | -3.2768 | -53.8199 | 2024-11-22 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 64739abc-a3ea-3706-b40a-bbf73949733a | -3.2385 | -54.2431 | 2024-11-22 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| f6d9a754-c810-38c8-9b1e-99742c6fada2 | -3.2569 | -54.2426 | 2024-11-22 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 35d7fdc7-1565-37d3-baf3-e91ce5012b79 | -3.2386 | -54.223 | 2024-11-22 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 89c2a3af-ecc2-3102-a568-67240a52eb15 | -3.2201 | -54.2436 | 2024-11-22 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| fae6f04c-73bc-3799-94cc-f5c6ea49af6a | -3.8535 | -52.3596 | 2024-11-22 06:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 952860b7-086b-38bf-b923-3d95afab36ca | -3.8719 | -52.3589 | 2024-11-22 06:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 57828584-1661-3930-9816-47bb1350fad7 | -3.2384 | -54.2632 | 2024-11-22 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 4a5c182c-bca8-3b81-93e5-25cc0df92c9e | -3.22 | -54.2636 | 2024-11-22 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 720f269b-a2c5-36d7-af4d-e81e4605f83e | -3.3451 | -50.5126 | 2024-11-22 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f6aa66fd-2e0f-397a-a41e-699a4e856044 | -3.2384 | -54.2632 | 2024-11-22 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 75343bf7-5571-368a-9390-dfe918d3bffe | -3.22 | -54.2636 | 2024-11-22 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 53f3c873-b0c4-3e7d-9b7d-fde6df5064d4 | -3.3451 | -50.5126 | 2024-11-22 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 128c0ead-47ca-3993-8867-6cc15f185529 | -3.2201 | -54.2436 | 2024-11-22 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b6c64a48-2dd3-35f6-90e2-01923ba3818e | -3.3452 | -50.4917 | 2024-11-22 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5e6772c4-8bf8-3de5-846e-b75a370dac7f | -3.2386 | -54.223 | 2024-11-22 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 16518085-cefe-35fb-bdfc-db5a2baaf9cc | -3.2569 | -54.2426 | 2024-11-22 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2e7c5aee-bf3c-3225-8750-4c2d4e9bf743 | -3.2385 | -54.2431 | 2024-11-22 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| ba604007-1949-3ca2-9861-24985c300c03 | -1.2041 | -51.9478 | 2024-11-22 06:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 118a62f6-eb82-351f-86a0-eb3e30491b4c | -3.2768 | -53.8199 | 2024-11-22 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| eb278fa9-5a20-3933-89e3-f9171a556956 | -3.2768 | -53.8199 | 2024-11-22 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e216f52e-a700-35fd-95e9-e4723705d70a | -1.2041 | -51.9478 | 2024-11-22 06:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 456bc157-cd3d-336a-bcb2-fb1173387a85 | -3.22 | -54.2636 | 2024-11-22 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d347168e-08c4-348a-a6c6-7f245a6508f2 | -3.2385 | -54.2431 | 2024-11-22 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 1574d1b5-3560-34ee-9289-9bc62c4727ec | -3.2386 | -54.223 | 2024-11-22 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 72e29fed-2f27-3168-990f-9d0b95e88f32 | -3.2384 | -54.2632 | 2024-11-22 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2b3c12cd-34ec-3e1a-8f31-0bfdd4fd73ea | -3.5159 | -53.8132 | 2024-11-22 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f66614f9-c2fb-31fd-a117-c8fc1bf893af | -3.2569 | -54.2426 | 2024-11-22 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7ac7c754-6606-3812-9b9a-a15ceb326ba6 | -3.2201 | -54.2436 | 2024-11-22 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 73c00394-4807-3504-bf16-d53fc3e04792 | -1.2041 | -51.9683 | 2024-11-22 06:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a236e749-b304-3743-a528-db512ad555fd | -3.3452 | -50.4917 | 2024-11-22 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e0197bf8-6f22-34b1-a04b-f6acfc24d992 | -3.5159 | -53.8132 | 2024-11-22 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9e1bd0d3-a083-3284-bdbf-c80aa9bf95eb | -3.2569 | -54.2426 | 2024-11-22 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0864cdba-9eb7-39dc-ae7e-b4bdb2c2f358 | -3.22 | -54.2636 | 2024-11-22 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f31339d4-983e-3e00-bd94-4652e9d3ebab | -3.2384 | -54.2632 | 2024-11-22 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e2f611d5-d38f-3085-a13a-c93bb7bf2aa9 | -1.2041 | -51.9683 | 2024-11-22 06:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f66522b6-070a-3e67-8bc0-827be7fd15e7 | -3.2768 | -53.8199 | 2024-11-22 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a5cec4d8-40cd-391a-b45a-4c7c75515d1e | -3.2201 | -54.2436 | 2024-11-22 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ee02d137-13dd-3692-ac1f-349e453e597e | -3.3451 | -50.5126 | 2024-11-22 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 594d8f73-49be-38a7-a464-ac704b9e39f8 | -1.2041 | -51.9478 | 2024-11-22 06:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f88bf28f-a79c-3369-9141-fc7b5e44fc69 | -3.2385 | -54.2431 | 2024-11-22 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 08bbd50c-a134-30f3-8bf5-d76a3c619127 | -3.2386 | -54.223 | 2024-11-22 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c6cfe20c-9bee-3c9c-b998-d48d140aa555 | -3.3451 | -50.5126 | 2024-11-22 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3bd8c107-fd58-3969-ace3-9d498ac4806b | -1.2041 | -51.9478 | 2024-11-22 06:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 50fa00fb-3774-382e-b771-bab35a686466 | -3.2201 | -54.2436 | 2024-11-22 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| c7aea3f4-d0c2-3d8a-a7b5-3aeb828916b5 | -3.2385 | -54.2431 | 2024-11-22 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| d2198288-8508-3083-870c-e91aafd31548 | -3.2569 | -54.2426 | 2024-11-22 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e7b73453-116c-37fa-90f8-7a3ba1658836 | -3.3452 | -50.4917 | 2024-11-22 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ae799ac3-8d4b-3862-8f47-a381b9e07311 | -3.4975 | -53.8137 | 2024-11-22 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d1734bd9-ed02-34f6-aa55-09828caeb8e0 | -3.2384 | -54.2632 | 2024-11-22 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ad2a1685-d267-3bb1-9e5f-ff7ab3c9901c | -1.2041 | -51.9683 | 2024-11-22 06:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 3cdc0778-24d1-32a9-9aaa-a94c12e579e2 | -3.2386 | -54.223 | 2024-11-22 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 83c8c564-2b82-3bf7-bc61-5369700867e2 | -3.516 | -53.793 | 2024-11-22 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 71978309-f8f4-329e-a4a6-be4098ef3ac0 | -3.2385 | -54.2431 | 2024-11-22 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 67449850-7872-3bc5-a24f-3530dbdbed41 | -3.2384 | -54.2632 | 2024-11-22 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ee38e27c-0b84-35d8-b516-089556b1e23e | -3.2768 | -53.8199 | 2024-11-22 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| de80f568-2b41-35a0-8d82-731c10f3f2b0 | -1.2041 | -51.9478 | 2024-11-22 07:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 729341eb-fbbb-3693-95c1-340ecc3c2623 | -3.2569 | -54.2426 | 2024-11-22 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| db7a86bf-441f-3bbd-a188-b498b5b9cb3f | -1.2041 | -51.9683 | 2024-11-22 07:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 67441875-2a5b-3623-867b-7f0cb4f73882 | -3.5159 | -53.8132 | 2024-11-22 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 82962792-ee62-331e-8f1f-f16e07c57ee2 | -3.2201 | -54.2436 | 2024-11-22 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| df9aad39-e3f4-3167-b7a4-2423ad6e70eb | -3.2201 | -54.2436 | 2024-11-22 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| dade4d73-bcac-3138-96ce-d2773034a2ed | -3.3451 | -50.5126 | 2024-11-22 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2758db73-a76b-3d68-875e-0496d7e58d8f | -3.2384 | -54.2632 | 2024-11-22 07:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c67d58b6-68c4-3f62-a799-56bc00f7e005 | -3.2569 | -54.2426 | 2024-11-22 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 29f8b75a-790b-3a14-af74-7d202db3fdfd | -3.2385 | -54.2431 | 2024-11-22 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 17683028-5b74-308f-a4a6-9cfbe1570117 | -1.2041 | -51.9683 | 2024-11-22 07:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1a3f4b8f-33ab-38cd-8ff4-7ec1252cba6e | -1.2041 | -51.9478 | 2024-11-22 07:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 98ef9ecc-3a9b-37e2-9dac-8bb6b7c3831f | -3.3452 | -50.4917 | 2024-11-22 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8d9fa98f-56b5-309c-abc1-0fb2272dcaea | -3.2386 | -54.223 | 2024-11-22 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 82b4e6df-c31f-34b3-b0d7-b5d4eefef166 | -3.2384 | -54.2632 | 2024-11-22 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| dde13d3a-8a11-3cc1-8962-b30f9c171ea8 | -1.2041 | -51.9683 | 2024-11-22 07:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0b42467a-2a6f-3487-beac-24796f042aa3 | -3.516 | -53.793 | 2024-11-22 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1681d979-5f18-36e2-af9c-aa185252cf28 | -3.2021 | -45.2932 | 2024-11-22 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 89317baf-5913-3958-b3f1-79eda0775ce0 | -3.2569 | -54.2426 | 2024-11-22 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1da0a472-f6a6-36e1-ac04-de395386be3a | -3.2385 | -54.2431 | 2024-11-22 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 592c3b5f-dece-3d33-9c79-fe269a8b557a | -3.2386 | -54.223 | 2024-11-22 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 263ec561-505b-36f0-89b1-5f57f98920e1 | -1.2041 | -51.9478 | 2024-11-22 07:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 99fedb80-fbee-313c-a083-f553c0a68c2f | -3.2201 | -54.2436 | 2024-11-22 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 52cc4800-38f0-3ae3-b068-944c8ac4f5d0 | -3.2768 | -53.8199 | 2024-11-22 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9f73ccb9-c0cd-3585-b205-1a1f93f2bcac | -3.2569 | -54.2426 | 2024-11-22 07:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 01dc173f-8ade-306d-90cd-e88a9e181371 | -3.2201 | -54.2436 | 2024-11-22 07:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| cf466a56-c157-330f-9445-47923fcbc25a | -3.3451 | -50.5126 | 2024-11-22 07:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 92c642ea-f525-3368-90a2-0803e5f5f5f7 | -3.2384 | -54.2632 | 2024-11-22 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 011c58df-da85-3f3d-9c91-2ad01bea90b3 | -3.22 | -54.2636 | 2024-11-22 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 11fe7bb4-6695-3d0d-af5e-fc49dce9e02c | -1.2041 | -51.9478 | 2024-11-22 07:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a5df714a-18ff-3660-9242-276354ad9e25 | -1.2041 | -51.9683 | 2024-11-22 07:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1adc0aab-3593-3fa4-997a-db60dd0ee8e9 | -3.2385 | -54.2431 | 2024-11-22 07:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 1278d9ce-4179-3693-8f09-d614ed9fe747 | -3.5159 | -53.8132 | 2024-11-22 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3e41f2ad-39fa-3169-9d31-0c0b07cd3da3 | -3.2768 | -53.8199 | 2024-11-22 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0b768289-6dfd-3782-af88-ce76a3b3a56c | -3.2384 | -54.2632 | 2024-11-22 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fa9f5ad0-e059-3a2d-9931-0164650430c1 | -3.3451 | -50.5126 | 2024-11-22 07:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b65851f3-c9f1-3040-8063-0716a2ad8825 | -3.2201 | -54.2436 | 2024-11-22 07:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 2ed47b30-b341-3156-9bde-c1bcb9e1b6f7 | -3.2386 | -54.223 | 2024-11-22 07:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0207ff49-96a7-3a2c-903d-c0ba15e0d6ea | -3.0536 | -45.2314 | 2024-11-22 07:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7aced282-8089-3db7-a0af-e09efdd28fee | -3.9104 | -45.0364 | 2024-11-22 07:40:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fbe3495b-8bf3-3986-9c19-3a65157cd2b7 | -3.2385 | -54.2431 | 2024-11-22 07:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| c17e8afb-94b4-3560-a607-f9c3b820ca73 | -3.3452 | -50.4917 | 2024-11-22 07:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 345da469-a8df-3c88-8686-73891d07e215 | -1.2041 | -51.9478 | 2024-11-22 07:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |


[Clique aqui para ver as próximas entradas](README68.md)
