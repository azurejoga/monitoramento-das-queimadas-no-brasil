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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cf46f27-be39-31a4-9911-41d4308f953f | 3.18283 | -60.68665 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2022f37-d5d5-3ea2-b65a-3b5bda24228b | 1.13109 | -60.52297 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 363a4369-972f-335e-9b38-4281452e2117 | 0.9595 | -60.53018 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01aa0371-e580-34c1-b088-a4c322378adb | 2.31893 | -59.87409 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5abdc87-9650-33b9-b907-2bcd8873923e | 3.15312 | -60.70314 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 777ebb61-fa0c-37d8-b01d-a97f5df375df | 3.15188 | -60.6954 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9f13f1bd-9ff7-332b-81ef-dd7a501846a0 | 2.5257 | -60.99275 | 2026-03-03 05:42:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2982dfa-7464-3935-a9e4-10b023695a56 | 3.03761 | -60.66014 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39d6d40-4f7a-33f0-9fbf-11f86c09e13e | 2.41478 | -60.70821 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16b9c484-2ef3-3e97-9aa3-2fc203ea6fd7 | 1.51181 | -59.92864 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46717200-e101-36fd-a23d-c5be113fa19c | 4.26882 | -59.89655 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46490e0d-709c-3cc4-a763-238a552b88f4 | 1.51622 | -59.93242 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6303e0d-bb19-3490-a091-6cdc283b7b59 | 2.77035 | -60.73601 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7cab1ff-e724-3653-9ed5-b11b4be24f75 | 1.07906 | -59.2539 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98fbcba7-6b1b-3f8f-abcc-b1787dde231f | 1.82853 | -60.84893 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b2505f8-b87d-347c-bff7-f96c9a28707f | 1.08217 | -59.24838 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62c0451b-0a79-3e2a-abab-1fbf3a221bfd | 3.57013 | -61.73463 | 2026-03-03 05:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bbcb034-f271-3501-8b1c-ec1beb3d36c8 | 1.55006 | -60.28631 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c49823-fabb-3adf-9164-26052fad254f | 3.15601 | -60.69876 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50533c75-89e1-3114-9093-c5e0eed80b67 | 3.11761 | -60.48178 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea7dfe5c-de7b-34f1-8370-a0121ea3ff05 | 0.47379 | -60.39546 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53a67b24-d0ee-3dd7-ade4-8b44d7c6fe1a | 3.16075 | -60.70592 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a5cb144-6e8a-337f-928d-7a6dd4f51f8b | 0.07422 | -60.54354 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76cce188-5095-3099-8af0-a7e2ab4e155f | 1.48509 | -59.92839 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9e6dc62-bbe4-3361-96fb-2a3d5ad26da8 | 0.44948 | -60.40808 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fe6cf9c-a824-3bb3-a5ae-3a20dc77384e | 1.35824 | -60.06634 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c8d6ca4-abef-30f7-b8f0-1ff33c54fce4 | 1.49783 | -59.91268 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1701ee8-61ed-348d-8138-d41112fa82c4 | 0.30585 | -60.44506 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f399f50e-1cbb-3546-a159-744937c234ab | 1.47765 | -59.92955 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dff63ab-96d8-3176-a30c-76b94c91e385 | 1.50902 | -59.91111 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4756cd24-4de0-33c0-96fd-427be0bf7055 | 1.35276 | -60.03128 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58d07f42-680e-39d8-985d-c92116b76395 | 0.30285 | -60.44992 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d25254-a80a-33de-a221-40eaf5b283a3 | 1.50669 | -59.92039 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a881e34b-f6af-3812-8a5a-30262c32cc5d | 4.0813 | -60.13995 | 2026-03-03 05:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4ab98d9-74da-34bb-9824-1229da9275ec | 3.17159 | -59.90816 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6353071c-4174-35ed-a81e-0f35cd279727 | 1.5095 | -59.93803 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49c9a54f-bdee-3213-a452-4fc9826e5ed4 | 0.49517 | -60.50604 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a3e3c3f-6c5c-321e-a2cc-327cde8dc1b0 | 0.05889 | -60.99305 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58af4ca3-3b66-3c0c-9977-7412505c1cda | 1.49853 | -59.91708 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 579d32e9-848e-3256-a29f-0d8723c032fc | 0.06246 | -60.9925 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a82a8566-6fa0-312f-91f9-b0fdee09392b | 1.5074 | -59.92485 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530da93b-a5ce-3ff3-bfb5-624904b4bad5 | 0.23481 | -60.51759 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 305ede07-1eaf-34e7-ba34-f5bf658c8cf8 | 1.45626 | -60.07104 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69cd6fb6-5c4e-3a87-9bb0-d830293f315b | 3.17646 | -60.69178 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84a07385-3412-343d-aff1-de89c054db95 | 2.90544 | -60.62723 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d17f83c8-dedc-3af5-8095-83ca60d3cb4f | 1.50458 | -59.90718 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bcd833d8-6649-395b-88d3-89130c764620 | 1.50155 | -59.91212 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ea55104-2da5-3a21-9705-bde1b8c8808c | 0.49746 | -60.49699 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c37d07-5806-324c-be43-8c85be2f6a14 | 1.50015 | -59.90331 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb53ba3b-5fe7-3416-8fe3-60c2bb22459c | 1.35888 | -60.05422 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2efd3563-05d1-3b64-a2b9-490cee35d66c | 1.47693 | -59.92508 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd1a9db0-48c4-3431-80cd-202c30f125d0 | -0.15557 | -60.74593 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d786ebb7-8ae3-351d-8656-f4676ec2f758 | 0.49381 | -60.49755 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0a8ef50-75bf-3cd7-b222-f706c1114ce9 | 3.93621 | -59.9814 | 2026-03-03 05:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eef6470b-e41c-336a-947e-543ec264b7f0 | 1.50972 | -59.9155 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c84f1ff1-e350-318e-b7e1-f32df89a7934 | 2.89486 | -60.62891 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a839d33c-e9a0-3afe-a4c6-3db28399739c | 2.81977 | -60.83681 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5369acf-d4cc-384b-8b4e-f96a4feaad8b | -1.51263 | -54.52744 | 2026-03-03 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 133b0bee-8a18-3a92-8047-287a287193dd | 0.92621 | -59.55896 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa4090c6-6cef-3a99-90b1-8f6535a9d303 | 1.96072 | -60.51608 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9366e246-b799-38a1-8e07-8d8f86fb93d6 | 0.69514 | -60.35064 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff4f315-9145-3366-92e2-77222f0da26f | 1.12681 | -60.51936 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00cdd3c8-73e1-3308-9acc-da9d75e5b826 | 1.8648 | -60.4002 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 069f54eb-d46e-3dc9-849e-91320aa94d93 | 3.03409 | -60.6607 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad62e4d2-71ca-3f7e-8f00-b9c667420c29 | 0.69932 | -59.96609 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d723ae04-bffb-3c02-bfc4-b0f6d81b0771 | 0.93331 | -60.31717 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2d890e-7f0a-3f25-b868-e4716bf3428e | 2.22559 | -60.74871 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cec06a6-0cb4-3def-ad36-281dbb21905e | 3.12116 | -60.48122 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b40fbdf-7f73-36b7-8a9f-afbdc941890a | 0.15305 | -60.49733 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a19284d3-baee-3ce9-bc26-87463f2b07c7 | 1.49108 | -59.91822 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 866ac3ac-227b-3622-8d19-b881dc055055 | 1.5081 | -59.92929 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e0f1a8-1958-3737-822a-b93c4494eaa1 | 1.97885 | -60.70005 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618a1688-7139-38f0-8576-67a857579690 | 3.17705 | -60.6955 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 035f01a5-7c61-3c8a-b806-fd8340a65642 | 1.07126 | -59.25512 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 989315cc-1070-33d9-b050-f72d5294f281 | 3.04752 | -60.65453 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f524403d-cd92-3741-84a7-58f42f4dd91b | 3.23881 | -60.13557 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfdbc8f8-a826-3c30-9662-43a07cc827da | 1.35345 | -60.0357 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c46a465c-6c0a-3588-a456-99c9757e6d39 | 4.27514 | -59.91249 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0aa9d2f-bc41-3fe9-b5eb-80bddc0d4181 | 3.98893 | -60.37907 | 2026-03-03 05:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46205a20-e198-3038-bc55-e9255beabc60 | 0.29986 | -60.45477 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5543584d-8c78-3cc7-a267-030ffee01e85 | 1.50226 | -59.91653 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 551cd8b1-d631-3eac-b260-2b57d92435a4 | 3.77759 | -60.12703 | 2026-03-03 05:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a256a8be-2c87-3165-ab57-8c87418573e1 | 1.51553 | -59.92804 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23244006-5034-36f1-9d96-0ef50dbce591 | 2.90608 | -60.63119 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0674b66-796c-35b8-9c09-29df7fae7d63 | 4.3671 | -60.54682 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94b9e8c-5dca-3f66-a0e3-613fb2e38451 | 1.48967 | -59.90939 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daff7554-83da-377f-96fa-8aa2340ce1be | 3.56956 | -61.73104 | 2026-03-03 05:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40024725-76d8-3e84-a8bb-0538a77ce24e | 2.61485 | -61.128 | 2026-03-03 05:42:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 706e5805-e715-320e-b1f7-6f56ba8bb7cf | 1.50085 | -59.90772 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8df8c06d-34a7-3001-9390-7b1f5a99ad3d | 0.87187 | -60.47348 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78963b25-95b8-3bdb-a611-546433052c1c | 0.49287 | -60.51507 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 329ccd84-ed1d-3cf6-9b0e-60e8de273641 | 1.4918 | -59.92268 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bd57ee7-282a-3bcd-854a-e7b48100a785 | 3.93557 | -59.97744 | 2026-03-03 05:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aeb6bd7-857b-3a18-aa5b-16b0720d89d6 | 3.63941 | -60.97917 | 2026-03-03 05:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76a1f42f-24b7-30c3-97f4-ed7a30ba3020 | 2.67645 | -60.41926 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4385f4bd-6231-33af-b11e-ba156d38b0a1 | 4.2645 | -59.89274 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1f4c9eb-5f2d-3a31-beac-00be309adb3e | 0.96675 | -60.52904 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57cf9ff0-c7f2-3d39-bbba-6083558a1837 | 3.05104 | -60.65398 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a18fa2a-9ede-3e21-b8d4-2f19c8ed8201 | 1.48437 | -59.92391 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5325ad4-1861-36ba-899f-5e8535a3bd24 | 1.64696 | -61.04926 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
