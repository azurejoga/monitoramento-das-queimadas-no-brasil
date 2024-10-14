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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd8ee617-e4c8-3850-9c22-15ae69ea38bc | -17.93835 | -57.34071 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 888c56f6-f0c7-3cab-996e-a32b9ef12bcc | -17.93757 | -57.34435 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 20b0df81-1c0c-3ff2-8d08-4e886e4eed01 | -17.93678 | -57.34798 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 612c1f9c-eadb-327c-9934-6f92b2859180 | -17.93669 | -57.34047 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 426141f6-d577-3db1-bc61-9c40f2bdee22 | -17.936 | -57.35163 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a06aafa9-6cea-3bd6-83a2-0e8577a8b3a3 | -17.93594 | -57.3441 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4bdb3faa-5e3a-3d92-a5e4-dd8da6995993 | -17.93518 | -57.34774 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 604e64c6-9355-34fb-9d88-38be233812a8 | -17.93442 | -57.3514 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a2dc0903-45ce-3e8e-905f-09436cac63f3 | -17.93296 | -57.33951 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00977da4-d3c4-3825-a531-977b9148ee24 | -17.93217 | -57.34315 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ca5cdc41-232e-33d5-9bb8-c43a18c4cc29 | -17.93139 | -57.34678 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e4218616-c78a-3a77-9926-11c87eaf3aba | -17.9313 | -57.33925 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 631f524d-eaea-3242-a5dc-a55dfdabe2d8 | -17.93061 | -57.3504 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6526c9e9-9260-32f9-84e6-56df9c710dd1 | -17.93054 | -57.34289 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 62354ee4-ad66-363b-a7aa-9e401101868b | -17.92979 | -57.34653 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d492de5d-dfa5-38b2-a2e4-87eda84f7fc8 | -17.92903 | -57.35016 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5f5cf0b3-3cfe-3946-8aec-48e0fa5c540d | -18.01917 | -57.3591 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 8ca31cb5-a6f6-335d-b97d-95612efc86fd | -18.0184 | -57.36274 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| e9ce6437-90d5-3781-9800-e25c439bea29 | -18.01764 | -57.36637 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 6e2a7b5c-55de-3e5b-b29a-d22906e6ed64 | -18.01688 | -57.37 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| bbf402a5-a206-389c-b945-a494c55edf7a | -18.01612 | -57.37364 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 895682f4-d8df-3747-beb7-8afc3621667a | -18.01535 | -57.3773 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 376421c0-d9a6-3348-995c-aa246cd3e4b0 | -18.0153 | -57.35062 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 6639b76e-0b11-35b5-8a47-a3130cb28357 | -18.01454 | -57.35424 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 371962dc-6e75-3565-bd3c-ddc8b740bf4e | -18.01378 | -57.35788 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 24ccf392-f5db-331b-92ab-3f38ffbcd51e | -18.01302 | -57.36152 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 2aa33a49-ca5f-3636-82bf-f55d0a974761 | -18.01225 | -57.36515 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 37feb458-c84d-338c-9f1d-149654c111fa | -18.01073 | -57.37241 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f213e086-e7d8-3281-aac3-f4b3033e1738 | -18.00996 | -57.37607 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 70d9845a-ccf8-3a61-8709-e5d260936e2e | -18.00992 | -57.34939 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 53da1497-234b-37b1-8eb9-202142115586 | -18.00919 | -57.37972 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e5cca966-42aa-36dc-9d87-20e680a00a5a | -18.00916 | -57.35302 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 5d4aa092-07a6-3bf4-b7d4-61a6aa166ca7 | -18.00839 | -57.35665 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 6570bd85-345d-3e85-bdac-b3076a7ac52b | -18.00686 | -57.36391 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 7c8c039f-4b02-3b64-b819-2e63a7077f08 | -18.0061 | -57.36754 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5e5cb961-5002-33f8-911c-286b951d4678 | -18.00606 | -57.34091 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c47972ad-d01b-31a4-ba7a-5ffe0fa1fbb7 | -18.00533 | -57.37119 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0aa4f11b-4927-3fe2-bac3-a326d8d299e9 | -18.0053 | -57.34453 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b5a9a4f6-83a1-3b3a-9e86-d151b29eb525 | -18.00456 | -57.37482 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 54f47945-9660-3cff-ae23-7f34c49d7166 | -18.00453 | -57.34815 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| b93c2220-a99b-3bc9-9077-5609ef3ccf27 | -18.0038 | -57.37849 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 91f48cbe-5d45-311b-9830-9a9be68c4def | -18.00377 | -57.35179 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| e65c5b5e-1242-3973-b5df-59a11616ab72 | -18.00303 | -57.38214 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 779e3ad5-ef57-3998-887e-f433d4efbf8d | -18.003 | -57.35542 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| a5e9552e-b762-374f-a594-af0570ed59ec | -18.00224 | -57.35905 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3ab3e4ca-a015-34df-8dec-31c596a201ad | -18.00147 | -57.36269 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 427c4aa8-ae08-3957-8f8b-8472218055ac | -18.00072 | -57.39309 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d6bcb1f3-2b6a-359b-8114-219eceae7e8a | -18.00071 | -57.36631 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f018c9f3-e940-358b-9dff-3f5d4f07fbdb | -18.00068 | -57.33968 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| fa3003be-618c-374b-8e86-0fc1c4196537 | -17.99995 | -57.39674 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 31e568d5-8554-39c5-9f53-d59f1770614b | -17.99994 | -57.36996 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8bc68a64-c1ca-324e-a0dc-2ef164339cc3 | -17.99992 | -57.3433 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8f83d510-ce08-3832-a0c3-eb0ea833c8c8 | -17.99917 | -57.3736 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 50a9f2e9-2260-33d3-93f6-7ccaba9a6988 | -17.99915 | -57.34694 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 1fe66665-7f9e-3a52-bb35-f10f3d902779 | -17.9984 | -57.37725 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3ee83dee-e30a-3e41-aa92-b365c8055454 | -17.99838 | -57.35056 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 3e90328c-2d41-315c-8ab9-21ff1d3502c8 | -17.99763 | -57.38091 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5961658-3578-3fae-89a9-dea4101a22a6 | -17.99762 | -57.35419 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6abf986a-b042-386e-b009-3f5115e07784 | -17.99685 | -57.35782 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 291587a4-319e-3573-a309-3a452dc4e14f | -17.99609 | -57.36144 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 84947770-85aa-3c50-8777-f7c043a9e85d | -17.99532 | -57.36508 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2c81e73d-1853-3329-98f1-52349e5e389b | -17.99529 | -57.33846 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 596a4013-ce9c-36aa-84d4-733cac18fd67 | -17.99455 | -57.39552 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 235fcc34-912b-331d-884a-bc30d49032c6 | -17.99453 | -57.34208 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 654a3918-0d12-3d94-ae9a-bb54b4d61c9b | -17.99376 | -57.34571 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 618b52bd-3a47-3d0c-b748-ac0d207adcd6 | -17.993 | -57.34933 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| ac487ffb-2975-3ddb-8071-1d2bf8f178f0 | -17.99224 | -57.37967 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1ee5cabd-82d3-385a-8387-9b28ad67a3f6 | -17.99223 | -57.35297 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| b98a9aec-f70f-300f-a4e1-2c6dbeb38964 | -17.99146 | -57.35659 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| e0e80b5c-6af5-3017-bc3e-731127d78e7d | -17.99069 | -57.36022 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6a79cfd4-8028-3361-8a2e-a9c1a9058b25 | -17.98992 | -57.36386 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 23b187e1-e7f8-3406-a607-344e16ea1dde | -17.98991 | -57.33724 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d024836a-401b-3be5-ad97-687a5583d770 | -17.98914 | -57.34086 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ed43c0cd-32d4-312f-af54-f10ad735093d | -17.98838 | -57.34449 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 1f1849b8-d5ee-3d99-8de6-feecb3d7fdb5 | -17.98761 | -57.34811 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 886e9499-b300-31d1-a366-1036f1d358af | -17.98607 | -57.35536 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 74cc91dd-df6c-3664-b3fd-ffa33a1a62bf | -17.9853 | -57.359 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4b3d71d4-ef1b-341a-a227-e5d2d65f96c1 | -17.98453 | -57.38939 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d01fa51a-971c-39e0-b385-290426e5212c | -17.98453 | -57.36263 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 31442814-173d-3361-8188-12e352cdc345 | -17.98376 | -57.33964 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ef127e8b-e505-3b08-848b-324ce8205f53 | -17.02978 | -57.43245 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 54ea4d00-c2bb-306a-ad40-8cec06c0877f | -17.02819 | -57.44009 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f6caad85-8563-386a-869f-191b00212017 | -17.02506 | -57.42739 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 67b2feb2-ff87-3b90-bde3-3c0eee39dcb6 | -17.02427 | -57.43122 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d29e8e26-a8ee-3887-95a5-a4badd249d2c | -17.02347 | -57.43503 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 886488fb-5ef0-3d9c-86ad-8d3c2abc43f0 | -17.02267 | -57.43884 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cb83d826-6eec-3609-afd9-81cc78d04f01 | -17.02187 | -57.44267 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c0b5a89e-a65f-3109-9816-adec5f9c355b | -17.02114 | -57.41853 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e1650c28-f1ea-311e-a4d9-a98c1599297b | -17.02034 | -57.42235 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9a6479ad-b154-3e3c-bbe9-29df44429dba | -17.01955 | -57.42616 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9367ac6b-c8e4-31c2-865d-db95edbdc25a | -17.01875 | -57.42997 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| adedffbc-cc05-3ad4-8efe-6b7aa4f171de | -17.01795 | -57.4338 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5c624d11-f36e-360b-a916-74fae92d36b6 | -17.01715 | -57.43762 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fd02a244-98f5-31ba-8bf1-ab4f85ee417a | -17.01643 | -57.4135 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e736138d-5b3e-3b24-8801-c5d967eb892d | -17.01635 | -57.44144 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c8aed8a-5c0a-34a6-9b2f-659a9d8639f4 | -17.01563 | -57.41729 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2f0411c5-f0af-36c5-b671-3871a54d52f8 | -17.01555 | -57.44526 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e3adb1bf-9071-3e80-b78d-999de9ff586d | -17.01483 | -57.4211 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b01c185a-b043-3ae4-b605-cdb778713853 | -17.01403 | -57.42492 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 346c4823-e4fe-3f40-bf28-1581c4824239 | -17.01323 | -57.42875 | 2024-10-14 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README62.md)
