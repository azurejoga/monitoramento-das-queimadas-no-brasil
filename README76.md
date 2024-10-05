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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b04314-06df-385a-a2a6-afa2df1b79fc | -16.16617 | -49.26698 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0565b21-6df8-33a2-bdda-f2da2c513491 | -16.15943 | -49.26121 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6fbe0ce-5021-3ae6-aa61-151122eb0834 | -16.1586 | -49.26582 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2af76fe6-4163-3ea6-9a5f-de27786c7cb4 | -16.15778 | -49.27044 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5dd0f8f-6580-30e0-9776-978d43f728cd | -16.15539 | -49.26313 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56e74af9-b20c-3f4a-ac07-ff3d4f231ae2 | -16.15483 | -49.2652 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 110612dc-aa65-314c-a8f8-5a2339c05bfe | -16.15459 | -49.26773 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fdc7a18-d3ba-33c6-899c-8f99a63cee0d | -16.154 | -49.26981 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3719663-eadf-329c-b3db-86c84857ca1d | -16.15379 | -49.2724 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47d54685-4b8c-391b-a775-cbb29bcf915a | -16.15316 | -49.27452 | 2024-10-05 04:17:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6f9ba1-cce9-344d-82ff-9f9ab48481b1 | -16.13115 | -50.44774 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5a2747d-ba44-3ddc-bb82-96b7cbf45619 | -16.13047 | -50.45152 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d333c4b8-955d-3f75-8b28-0fdc49457dc6 | -16.12975 | -50.43233 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1794c2f-17d2-36b9-b9de-5d08c6d1bcda | -16.12847 | -50.43942 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b0e50b3-7049-34fd-8591-37d976cc7615 | -16.12715 | -50.44673 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff08f29d-ebf0-3d6a-85f9-7f1e77a955f9 | -16.12647 | -50.45052 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec86bd76-8c9f-3b8b-8d3c-71e3745872e1 | -16.12576 | -50.43133 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56aadad9-42c9-34ce-a56c-755cc37f25b3 | -16.12514 | -50.43478 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c728b99-1b7a-3d0e-8dac-93a2f88c44fa | -16.1218 | -50.45329 | 2024-10-05 04:17:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de84020f-b90b-390c-850d-e7d656a60650 | -16.11173 | -50.46277 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e815e5-ab76-31b9-8d27-b1ef4f7f01e5 | -16.11103 | -50.46663 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ec95351-186b-3805-86d3-dcd0a953cbd6 | -16.10772 | -50.46187 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dff07aea-8adb-3f14-9562-8fbcadff797c | -16.10701 | -50.46577 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ec626e-d244-3307-8d19-51c4468a0aa5 | -16.10476 | -50.2503 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8253f06d-4756-39fb-8789-3b3ca414750f | -16.10381 | -50.25548 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8dc7373e-3038-3894-8606-c282863d5998 | -16.10298 | -50.46493 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d220145-404a-36d0-b7ef-ed380325fd97 | -16.10228 | -50.46883 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02901d3d-a56f-3831-b576-81afa3b13675 | -16.10085 | -50.24913 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac5b72b4-018c-3c23-accc-64a62bb4cb02 | -16.09899 | -50.25927 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 538e150a-709d-31e0-afb3-76477088e816 | -16.09895 | -50.46415 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a6d7514-9ab4-304c-a0ab-2891291aad36 | -16.0988 | -50.23782 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64fc3a36-8a14-3b7e-a1d5-c5bef467e6cd | -16.09824 | -50.46804 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7f9ab15-7635-31cd-a625-5f0c4141638c | -16.09786 | -50.24291 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d487e066-67fd-35cd-a79b-b30b59c257f4 | -16.0949 | -50.46341 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c0232f0-c5c7-3cbe-8d8f-fcffdca432b5 | -16.09485 | -50.23689 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03ac7f12-9fc5-3af6-8637-cafa82cc51d5 | -16.09419 | -50.46728 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a4580d4-6f63-344c-9cb5-af09201f7ccb | -16.09396 | -50.2353 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff84015f-5018-367c-a46f-850c9b96e8f2 | -16.09305 | -50.24043 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79083c3d-9d62-30ad-bd2c-e33792a5932b | -16.09154 | -50.45889 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de45d4c8-db19-30a9-837b-26bdf8eec57c | -16.09113 | -50.43827 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 541d3482-b278-3160-b837-35509b118602 | -16.09084 | -50.46276 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6ac830d-ee30-3da0-8ffd-2711bec625a2 | -16.08995 | -50.2411 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ac73aa0-6fad-3c84-ab01-d61df82561f3 | -16.08961 | -50.44658 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 614380da-3b94-39b1-b5ce-31bf0484b0b6 | -16.08909 | -50.23956 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64c67371-3661-3327-9164-ab640b55498f | -16.089 | -50.24629 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1712b52e-06ff-3bf5-9567-db55845a28ac | -16.08888 | -50.45056 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79ebfc38-e189-34be-afce-0b1eb83a76fd | -16.08817 | -50.45448 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfde0465-8d5e-37e4-9ac0-e4197687989a | -16.08817 | -50.24472 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 11004bb9-31e0-3fae-9884-5f9bde91cec4 | -16.08696 | -50.43823 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a0ccbfb-d411-3515-82dd-117f39b57a51 | -16.08624 | -50.44219 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 649645cf-f89e-3565-b362-eeeeee467be5 | -16.08618 | -50.256 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 798d107f-1c20-3d05-a9ea-42a32a5de51a | -16.08596 | -50.24038 | 2024-10-05 04:17:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd08d50f-718f-3a51-b347-16f73d849d97 | -16.08552 | -50.44611 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48f9361a-8fe8-3297-ad21-01674951f3ea | -16.08522 | -50.26143 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 875e4528-83e1-3cc2-ab6a-738b850124ef | -16.08496 | -50.24579 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2b09946-4cb7-349b-a52b-f2576b6084af | -16.08482 | -50.44997 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc3952b9-37d4-33ab-8ff4-ef40dd56d3f1 | -16.08414 | -50.24428 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f7f6141-6509-3033-8762-eaac6b4cfd1b | -16.08412 | -50.4538 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 705b9e8c-4923-3db4-9604-615d9f7b0541 | -16.08312 | -50.24999 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ec7f383-6e4f-30ff-b571-72618faa3764 | -16.08287 | -50.25712 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83fac294-3940-324d-bf5a-bf5ad8bcd82c | -16.08216 | -50.44169 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6da67c5a-2b48-386d-8f41-9db0123b833e | -16.08212 | -50.25566 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8303fe09-8d77-3c80-99d9-53178f853782 | -16.08187 | -50.26252 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79d82757-e790-30d3-9aca-2a9f0e0cb298 | -16.08146 | -50.44551 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93d5540b-7a28-3c60-8ae3-e9643daed852 | -16.08089 | -50.2455 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cdfa762-8e32-3a40-a771-156c7e77f56c | -16.08088 | -50.26792 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bfb3b98-dcdc-345e-a2d3-c23e84d273ae | -16.07671 | -50.44861 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4f6c76a-d44e-377b-a8fd-e08bc57c0b9b | -16.0763 | -49.71844 | 2024-10-05 04:17:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe1d3d7c-5ba7-376d-a7f0-3aa7baaaa928 | -16.07302 | -50.23732 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 600ae274-a7fc-30ac-a65e-17559686f446 | -17.6917 | -43.79338 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06a80040-d69a-35c0-828b-4bf6e136b9a7 | -17.63742 | -44.32365 | 2024-10-05 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bec3a62c-c55a-3aa0-b52b-8d4a27ae71ab | -17.63516 | -44.31569 | 2024-10-05 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5915a351-f2b1-3b4e-a668-c8a42c0205cf | -17.6346 | -44.31941 | 2024-10-05 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c584e2-9e72-3aef-aa13-2c26a0888fca | -17.62015 | -43.26514 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0627880-6f0d-30a0-a4b4-e1b5ba6353e0 | -17.61779 | -43.25689 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 366c7f0c-0040-34b4-9c0d-dac0423495e9 | -17.61723 | -43.26075 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc7ec885-d624-3aeb-a6a0-881262affeec | -17.6143 | -43.2564 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 497e2ff9-1011-303a-a0c4-3372c1d63dfb | -17.61373 | -43.26027 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 20714d4f-d4ca-34c9-ae45-7e96f4671cfd | -17.61317 | -43.26414 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1828355-8dce-3059-af9c-929d9cb68404 | -17.42439 | -44.94461 | 2024-10-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae97b7a9-9e3e-3f5f-b357-144d2d416949 | -17.32148 | -42.37003 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68d4a4e1-b90d-3f18-922f-2c832e60ad7f | -17.31912 | -42.36065 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c313c8c-653c-32f6-8b06-f6b6a3950b2b | -17.31304 | -42.37749 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e1b8c3d-98a2-3a32-97f9-4d03f6bb677e | -16.97007 | -44.76246 | 2024-10-05 04:17:00 | NPP-375D | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0f5e38f-da89-3415-be6c-f8047544e6b6 | -16.96951 | -44.76609 | 2024-10-05 04:17:00 | NPP-375D | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7d7d8ba-5156-30f3-9645-754503df6717 | -16.68211 | -43.88524 | 2024-10-05 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33ee0975-abda-32af-aef5-92c35d55c78d | -16.47671 | -43.81506 | 2024-10-05 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 108b80da-3147-3ea2-bdf5-6f606e5177a4 | -16.47612 | -43.81894 | 2024-10-05 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e9e19d4-dbfb-3b4b-9008-373c7cb45ccd | -16.34832 | -43.69442 | 2024-10-05 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05aa6c14-5b77-388a-929e-408d1359d41e | -16.18094 | -43.64928 | 2024-10-05 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4af8e3eb-587d-3c2d-9727-5a6bbbdf5910 | -16.17754 | -43.64874 | 2024-10-05 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da7efcc1-52e5-3c84-93da-47b04be75b03 | -16.15331 | -44.2268 | 2024-10-05 04:17:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8c8249-4913-34c9-b178-77119f4c5ceb | -16.05685 | -43.80289 | 2024-10-05 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 461b8a3c-1865-3e10-8fe2-3a915cf79f09 | -16.0529 | -43.80607 | 2024-10-05 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5dea1d8-efa4-32fe-b0dd-5da5433971a8 | -16.0148 | -43.19855 | 2024-10-05 04:17:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9bffd25-b704-39dd-816f-799bda601ba2 | -15.85972 | -45.26754 | 2024-10-05 04:17:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7100e5c-2253-3224-ab93-88b38ebbec49 | -15.85916 | -45.27113 | 2024-10-05 04:17:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86bc147e-ccae-3e98-924a-8586359932de | -15.72493 | -44.83331 | 2024-10-05 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27df9727-e0a1-39e7-8c8d-087b7db7d621 | -15.52247 | -42.24182 | 2024-10-05 04:17:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d972fcec-18b8-38eb-a03a-3965b1e529fc | -20.07667 | -45.78539 | 2024-10-05 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README77.md)
