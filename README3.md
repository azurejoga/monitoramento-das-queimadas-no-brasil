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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3db6141-cbb6-3e57-be2b-839043af8850 | -12.33158 | -50.00927 | 2026-05-05 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 55f6df36-a86b-3a96-92d6-90d4a9fb4dd3 | -13.60887 | -44.38096 | 2026-05-05 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3831b317-a974-3fd1-9e3b-fbffc19dbda1 | -14.07435 | -47.62962 | 2026-05-05 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 001afbc7-c62e-35ce-a5db-49e730e2fd7c | -13.92287 | -47.2832 | 2026-05-05 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 708df5dd-fddd-3fe6-8cf7-af40f1101dcf | -14.03262 | -47.64585 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baed90e9-2741-35e6-a523-442c9f29f444 | -18.9348 | -40.17762 | 2026-05-05 04:06:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4200e345-47cd-3dd9-b767-37186e2b3c79 | -14.20389 | -44.27201 | 2026-05-05 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d7bae94-663b-3aaa-85ec-d94c8aa75b22 | -17.52387 | -46.71475 | 2026-05-05 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 539f3cba-032d-35a8-9aee-6b60de611a9d | -13.90855 | -47.52767 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84408f1f-b5cf-3604-bb7c-7255ad8b10c9 | -16.75642 | -51.87209 | 2026-05-05 04:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b818eca8-57dc-3c27-98df-79fc3038a405 | -14.03631 | -47.62659 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6743a75-784a-32f0-ad38-242ef6752f9b | -12.33719 | -50.01041 | 2026-05-05 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd526791-7b07-38dc-a605-83a923946794 | -14.05101 | -47.65085 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eeef915-3efe-3b8d-9f10-468f53976827 | -17.79884 | -46.71326 | 2026-05-05 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c280a93-e6e1-3926-ba5e-ca7c4ab325af | -13.43456 | -43.84534 | 2026-05-05 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| cdb756ab-2776-39e7-b2af-5b3e2558dbdb | -14.07865 | -47.79412 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c71cd2c-b1e8-39d4-a232-b9da2cb1e823 | -14.04822 | -47.66551 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b98c0716-f0d3-3ac5-9f88-4c40a60616dd | -14.07533 | -47.62441 | 2026-05-05 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd030cc5-f770-3d67-804c-e48dd141d6bb | -12.33794 | -50.00654 | 2026-05-05 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a24af3f0-f35d-3cca-888e-0c649d691bbe | -15.42129 | -43.05595 | 2026-05-05 04:06:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 38013020-031c-3a45-b89f-07595df29fd6 | -14.04092 | -47.62772 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beb590d0-3dd3-372a-bf6d-b5bae9c6d25e | -13.9649 | -47.50927 | 2026-05-05 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| add143ad-d639-3ec9-8ea7-c33a297c1df7 | -14.04545 | -47.65463 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4be46278-f2d3-3fdc-aab2-443487b53ed0 | -13.43828 | -43.84599 | 2026-05-05 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 57aec729-d3d2-3423-88af-cde0cf2a6e2a | -13.90997 | -47.53133 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17f8401-8b32-36e1-9610-4989d1b98044 | -14.07068 | -47.62348 | 2026-05-05 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b72a3067-06f6-3e24-9021-2e8780cd3aee | -13.97502 | -47.53181 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53223d22-db66-3ed3-83d0-c002201f6d14 | -13.96395 | -47.51424 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 072be8e3-50cd-32c6-829f-6ddf45964a18 | -13.60505 | -44.38029 | 2026-05-05 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6c9555d-bd58-3985-a57f-0454a78350c0 | -14.08358 | -47.79389 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 872d89b1-6737-361d-a766-30797320ae96 | -17.80294 | -46.7141 | 2026-05-05 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e119f12a-7cc1-398e-b53a-5cc6b8acfe44 | -17.79954 | -46.70952 | 2026-05-05 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8baa96be-8906-3450-b8bf-519c6abaeeb5 | -13.92749 | -47.28375 | 2026-05-05 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 640bcae2-3c6e-3c20-99e8-430ad1ccf510 | -14.05285 | -47.6666 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1374dc8f-3ee2-3d41-bc87-d91dcea3891d | -13.24145 | -44.4659 | 2026-05-05 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e748835-e365-33eb-ae10-823bc5a63fdf | -21.53387 | -47.13941 | 2026-05-05 04:08:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f22b0a24-f78b-3529-aa62-da25cc656915 | -20.93967 | -45.42189 | 2026-05-05 04:08:00 | NPP-375D | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32ab5750-8e59-3614-8be2-84894107fc48 | -21.52991 | -47.1386 | 2026-05-05 04:08:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b4dc6cc-dc1c-3176-8ce8-6a00671d36c2 | -22.80172 | -49.34037 | 2026-05-05 04:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 752bb611-d643-3c03-90af-a2eb45ed380e | -21.70394 | -48.41977 | 2026-05-05 04:08:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e64eae1c-6fa4-3d21-bca9-1d2e5a30b5f0 | -22.48722 | -41.95823 | 2026-05-05 04:08:00 | NPP-375D | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c494fb4c-b31f-3935-88fc-8f2fdbaf20f6 | -18.493 | -51.69193 | 2026-05-05 04:08:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3611c03b-713a-3d30-9439-284ffad35b56 | -23.36487 | -46.16839 | 2026-05-05 04:08:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e783a770-5831-38ff-af78-09277ba28314 | -22.79908 | -49.34132 | 2026-05-05 04:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d69850d8-466f-3196-b095-b391309cf2e8 | -18.49218 | -51.69569 | 2026-05-05 04:08:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 331fdc13-14e4-30f1-867a-59b1bdcb31a7 | -22.49055 | -41.95882 | 2026-05-05 04:08:00 | NPP-375D | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09141b07-d608-3b97-9b28-f450bd28def4 | -21.85916 | -46.97547 | 2026-05-05 04:08:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22e29e26-fc72-351a-8462-307698c85a6d | -23.56145 | -47.51962 | 2026-05-05 04:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bbf2174a-d2ec-3cac-9af3-ec9ac5629347 | -18.67054 | -50.22757 | 2026-05-05 04:08:00 | NPP-375D | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ed17b0e-b0ab-386e-ba58-572ae4cf4715 | -18.43143 | -54.7204 | 2026-05-05 04:08:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 911c5b1c-4628-3aaf-a445-f1cce3223cf5 | -23.4078 | -46.42259 | 2026-05-05 04:08:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 39142234-f952-33d0-8ec1-12ce2b78ca58 | -23.03843 | -47.7429 | 2026-05-05 04:08:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 86779398-577a-3801-9ce8-c6c4d88c1f64 | -22.67948 | -47.47316 | 2026-05-05 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e95d0d16-21ab-3479-bd57-94a5f7fae932 | -22.70168 | -43.36342 | 2026-05-05 04:08:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7d3df8a3-14b5-33e1-b64a-eead9ea18553 | -21.31849 | -48.69284 | 2026-05-05 04:08:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 55bf9d46-7a43-3b57-915f-008e50243012 | -18.6699 | -50.23066 | 2026-05-05 04:08:00 | NPP-375D | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 50862add-827a-35ad-9266-4b669ce883f0 | -22.28862 | -48.7841 | 2026-05-05 04:08:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 134bf593-fe75-3c3a-924d-f51d54a198c9 | -18.43281 | -54.71445 | 2026-05-05 04:08:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52534380-050c-387e-b414-d3f71782c9ec | -21.8569 | -48.06689 | 2026-05-05 04:08:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 053baaa1-cdc7-387b-b2df-8d4e6af88f7b | -22.74283 | -42.2547 | 2026-05-05 04:08:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cda26d1-d9e8-3f2e-8fae-cd8c56b74dd9 | -22.67446 | -47.47789 | 2026-05-05 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74a3bec5-f4ee-3858-9931-68576f110ea4 | -22.48381 | -41.96624 | 2026-05-05 04:08:00 | NPP-375D | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5042d9f3-5d6b-393f-8b38-5accf2355210 | -18.49498 | -51.69301 | 2026-05-05 04:08:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22a2bb37-41a6-3f7d-a805-c4d25007e07d | -18.43416 | -54.70864 | 2026-05-05 04:08:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e2a13b2-16a3-3153-8cd4-0ef4fb823805 | -22.48604 | -41.96573 | 2026-05-05 04:08:00 | NPP-375D | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e30b078a-6ab0-3b9f-93f6-8e0265452607 | -21.70311 | -48.42393 | 2026-05-05 04:08:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a91f27cd-c29b-33fe-a57d-1774892dd762 | -21.1933 | -48.81767 | 2026-05-05 04:08:00 | NPP-375D | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64a731a4-c07c-31fd-b460-a303856b7953 | -18.48937 | -51.69204 | 2026-05-05 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16916639-f53b-3e55-a91e-795a8d4d189d | -21.53783 | -47.14022 | 2026-05-05 04:08:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 113412c2-2359-32d1-8f30-bfe4619b4f6f | -22.29293 | -48.78504 | 2026-05-05 04:08:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 855e250d-8d0f-3266-9af3-a2c50dc0dd25 | -19.97801 | -47.20554 | 2026-05-05 04:08:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f233412-8e89-3dd9-bf8a-a12c85c8694e | -22.67841 | -47.47877 | 2026-05-05 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80611f6a-2caa-3ddd-accb-dde70f66b4e6 | -21.85526 | -46.97466 | 2026-05-05 04:08:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ace20717-79a2-372c-9178-b20d8208bfdd | -22.8286 | -47.15155 | 2026-05-05 04:08:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30ab6c53-2cd5-3e69-b4ea-a40d249440dd | -7.51145 | -49.42592 | 2026-05-05 04:21:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4cdcca3-b0b8-364f-b3ef-bce19745d238 | -7.51607 | -49.42368 | 2026-05-05 04:21:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6620d3a7-e2a0-315b-bdb6-4671acfc2839 | -7.27546 | -46.79337 | 2026-05-05 04:21:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ee2a82e-8efe-3297-872f-76af3a510ea8 | -7.51911 | -47.17023 | 2026-05-05 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32ca3307-d3fa-3486-8e6b-755021f33be8 | -8.20626 | -47.99203 | 2026-05-05 04:21:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d5f641-a4ec-30cd-a241-d3f60d0e18ab | -7.51535 | -49.4266 | 2026-05-05 04:21:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17618b44-dacd-3d7a-9a06-6d04259bf570 | -9.56892 | -44.57214 | 2026-05-05 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62c6ac12-95ae-37cd-bff7-f73683fae59e | -9.56615 | -44.56808 | 2026-05-05 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce15a0b6-49c6-378b-a6b1-9fab20f7c8ce | -9.5656 | -44.57161 | 2026-05-05 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd290b4d-842c-3a22-a6a3-a02cd827dde0 | -8.20337 | -47.98735 | 2026-05-05 04:21:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d69d7e2-ab78-30a8-b2a7-db6fef62415a | -7.87372 | -42.6883 | 2026-05-05 04:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90a9c067-2098-39d5-ad85-35b7996d8cae | -9.7644 | -43.89928 | 2026-05-05 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ea239ab-a355-37c6-a85a-25710ed26fff | -7.87661 | -42.69268 | 2026-05-05 04:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2932be16-761f-366c-9957-52fb56a86761 | -8.78241 | -44.82413 | 2026-05-05 04:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e43fe659-2110-3bf7-b79d-f26bd7651616 | -9.56282 | -44.56755 | 2026-05-05 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eee1ba0f-f18d-3f72-b094-ad28417031ed | -9.56838 | -44.57566 | 2026-05-05 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eca6c1b-6ec5-386f-a565-29bbeaf45eb3 | -7.51514 | -46.04367 | 2026-05-05 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a92c70-78f1-3fd5-ba68-d42f0e77a86c | -9.34582 | -47.09109 | 2026-05-05 04:21:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cd66e38-a237-3633-addf-382fd1b170a1 | -7.52257 | -47.17081 | 2026-05-05 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5fb4404-c136-3fd9-a5cb-b3825cd5dc7d | -8.72334 | -47.98204 | 2026-05-05 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f744caf-322b-30fe-a88b-f97731c57d8e | -7.52195 | -47.17464 | 2026-05-05 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea258f31-29b5-37f2-aece-e81192b4310a | -7.52542 | -47.17522 | 2026-05-05 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49e9f4da-ec76-3c02-8815-f0f031c042cb | -8.78295 | -44.82066 | 2026-05-05 04:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aa85d0b-2530-3633-8eca-0a70b0277ec5 | -13.99929 | -56.63861 | 2026-05-05 04:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb52588a-d853-3d5a-9098-459b20cd61bc | -12.32408 | -52.47722 | 2026-05-05 04:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c65facd1-d418-3780-9f1c-6282c8d1af7b | -11.12648 | -45.1189 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
