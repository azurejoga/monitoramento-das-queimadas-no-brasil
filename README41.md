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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55955fd0-a5c8-35bf-8d74-48b8a31af148 | -6.37355 | -42.78886 | 2026-09-23 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27669172-c542-336f-bd32-6f40e27fcfaf | -6.90044 | -46.57114 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe845602-7425-3ed2-b12e-258765adf4a1 | -6.61916 | -43.7324 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 70653ee6-58d9-3414-bcd8-8b7eb84938ff | -6.1329 | -43.84531 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f504f65-51b7-32ba-98b8-8cde8645e1ae | -5.60515 | -45.94476 | 2026-09-23 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f6f8c5d-25bf-362d-abec-8b207d744cc3 | -7.41709 | -44.73287 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 845a4baf-7491-31af-adf4-634b1f6da099 | -6.6039 | -43.75301 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc9d84f3-8c7b-3249-aa88-4e51aa0bb9b6 | -6.60669 | -43.73763 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 82b11072-98c3-3df9-b7dd-d326fa5bfba2 | -6.72052 | -44.15872 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 578adab7-e2bd-3ae8-9588-a4e9f87f06b5 | -6.6136 | -43.7313 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 690c0e96-9cc0-340f-a61b-b9d67d01c20a | -5.99156 | -45.24057 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bfb91aa-507e-33c3-826e-2160d6798ec4 | -5.76689 | -45.11985 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb1d1ca0-7765-3bf5-ad61-54ad75f0c70d | -7.97696 | -44.09693 | 2026-09-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cad4678-437c-376a-9d1c-2a224fb2b680 | -7.13215 | -43.07854 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e66d1e5a-65a1-39cd-aea8-7eb277b9ce7b | -5.99245 | -45.23558 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11b303e0-77ab-3230-ac0b-546d6b05b4e5 | -6.57824 | -44.15369 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56df85da-a836-363e-a7b2-588364a78318 | -6.98942 | -42.59989 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 04a33912-19e5-3c36-a42e-cef3d65e1d35 | -6.1004 | -44.15358 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8513a715-a661-3075-82b3-cf5ab179ca53 | -7.13532 | -43.0827 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f5fdc3e-d304-383e-a2a3-19031a9a9aaa | -6.38718 | -42.27843 | 2026-09-23 03:42:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e613c5ca-390d-354c-94a9-96dbe96f31b3 | -6.14306 | -43.84081 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6de79b8c-b699-33eb-a2cc-c08d43cc8780 | -6.10083 | -44.15103 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3a7c251-73e6-3c11-b346-a33dbccaf5f6 | -6.89042 | -46.55147 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca2894e1-3f1e-321b-9348-31436e653f39 | -6.61715 | -43.74354 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 957b6b44-bd67-3192-a983-b4a8d70e2868 | -6.61923 | -43.7639 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f483a46-3b80-3e4a-b1ce-5820c29c38d1 | -7.13005 | -43.08162 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a41b397-b8d1-34ba-b7bf-381ba5fe51dc | -6.60343 | -43.7341 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b09d4d9-5d16-3bf9-888b-cf15071e5362 | -6.72125 | -44.15461 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6301ad7c-fcc8-3df9-b8c0-08fac27798a0 | -7.03065 | -44.66 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8150afa2-0eb6-350a-9f99-c2a1b2759bb3 | -6.1709 | -44.12586 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7094c4f7-9fab-38b7-bb5b-af3a207590d3 | -5.76072 | -45.11872 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b9c04df8-3e24-3553-bdf2-dc6e6a78b112 | -5.99863 | -45.23678 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99fbca2c-77e7-3181-82e1-540d09bc29b6 | -6.10117 | -44.14935 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc67869f-8ddc-3f5f-b041-bb9559362d5f | -7.45944 | -45.49328 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0000478d-e2e5-3a4d-b442-e8f1fca7a23e | -6.60948 | -43.754 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f16b60d-ddfb-3b2e-90c9-43a118596b38 | -8.72816 | -39.64338 | 2026-09-23 03:42:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 29e783af-2533-376c-aa92-b9f86b8845b6 | -5.61937 | -43.36453 | 2026-09-23 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 932ae9a8-ded6-34a4-bc09-776ab5d2aa31 | -6.60318 | -43.75692 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3116a4f-a80a-318f-87f0-f40d47499525 | -6.61577 | -43.75114 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f5cb0830-480b-3ed9-a868-d4df2a1e5583 | -7.45824 | -45.49626 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 591210f3-23be-3c47-bcec-521518a9d724 | -7.02987 | -44.6643 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 26cc21ce-97b4-358a-8cf1-3bf6fe8ed483 | -6.52252 | -43.54541 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73326df4-571b-36bf-a33c-3919f0b75d59 | -6.13612 | -43.84714 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 63138bcf-1c3a-3e2f-8807-d75133528b21 | -6.92796 | -46.57037 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 352df523-4486-31c3-8e9e-4a80bb1ec612 | -7.15619 | -42.08656 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa3e7aaa-4249-39de-9e9d-ea560369986d | -5.34862 | -45.17085 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ef82781e-f571-3fbb-a56f-442b8c225233 | -6.97968 | -42.5949 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51a4c6aa-d18e-3ecf-bd42-371812d725e5 | -7.6505 | -45.44891 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5769ba8-ffbc-3c3c-81b0-8c5d408303a2 | -6.9247 | -46.57338 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb8599de-5f7d-3632-b051-2359e1d7a27e | -7.14234 | -42.07822 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b930062-ad84-34ed-9c3c-eb2037afe738 | -6.41523 | -42.83004 | 2026-09-23 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdf7bdf2-9d72-3014-98b3-8d2f3e47813e | -6.10699 | -44.15013 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e9068f9-91ae-391a-a3f9-45e9eb78c4db | -6.92698 | -46.56141 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7871e61-13b4-397c-9d3e-9b371a7c9808 | -5.34948 | -45.166 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41dbf313-fd48-306e-9612-710e2ab23256 | -6.57968 | -44.14564 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3526ab8c-46f0-3b56-903e-670e8c77e037 | -5.56475 | -42.73109 | 2026-09-23 03:42:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6e9b62d8-b30e-344f-ae31-d69f0e0b6b84 | -6.61436 | -43.75895 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed2102dc-55c8-3b09-95e5-2f3e5b0feb63 | -6.59622 | -43.73184 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d0ff5f0-dc0d-3ceb-bb96-a70843b95ae4 | -6.32594 | -43.93565 | 2026-09-23 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 140ade84-0613-334f-86a7-df65dc6d8e57 | -6.42847 | -43.72309 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa94b5dc-cfed-3217-a13c-4997fac9491d | -5.41959 | -37.71009 | 2026-09-23 03:42:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5ef976df-893c-3ac1-9d3b-6d51c0dffcb5 | -6.62203 | -43.74842 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b597bb6-39ce-34c4-b4af-0a25df041732 | -7.31487 | -42.26635 | 2026-09-23 03:42:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e649809c-dac4-3049-b352-f4e0abcf3c60 | -6.89779 | -43.63605 | 2026-09-23 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bce17058-27a0-32e3-bc79-206102e789cf | -6.60278 | -43.73784 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c01f1869-2417-3a33-b3c7-423b8553b563 | -7.03217 | -44.6516 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 50d6b668-88d1-3ee7-b515-0822198bd115 | -6.38666 | -42.28144 | 2026-09-23 03:42:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bec9f190-65ea-33ac-a4c3-411217dfe7ad | -6.6185 | -43.73609 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 73386f0d-69ed-3eda-9fca-a024a62d7193 | -7.4586 | -45.4979 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0277d66b-624f-3e0b-9157-7756f3dec11b | -7.18333 | -39.32572 | 2026-09-23 03:42:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0ed994de-c053-3391-a181-a98eca2a16c8 | -6.60044 | -43.74034 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 4c438b61-8a1b-3fdd-942a-990d0e6f1a01 | -6.93348 | -46.56324 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 177ec0e8-1365-3b39-a3af-8196fc61d028 | -6.59721 | -43.73678 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aafd9af5-3ea4-32d5-b855-e6e99dcba7c8 | -6.18451 | -45.32397 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae749caf-a47a-3d7a-b127-1b79c8682e9d | -6.92686 | -46.57633 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b7a6982-f0dd-35c3-ace9-87342e2e8205 | -6.13986 | -43.8392 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 55813b9e-d45e-35fb-bc06-10a77a3d10db | -6.89591 | -46.55873 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8894c9c-4627-3742-9dca-7ed15fc145a5 | -6.72337 | -44.14941 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63c117ef-2b14-3ac4-abaa-a38ead57bbba | -6.52731 | -43.55038 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5749451-8e80-3f18-970c-7792097f35c1 | -5.99754 | -45.23466 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd114036-657c-3cfb-981b-7262069ee217 | -7.49655 | -44.33411 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89940ffc-ef44-3196-aa2c-a0635e1b2d3e | -6.3741 | -42.78572 | 2026-09-23 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f0e7934-7719-368c-8d6e-0949e3233db8 | -7.13125 | -43.07504 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 33187399-417e-3d37-bdda-48a61c9591c8 | -6.21901 | -41.6805 | 2026-09-23 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4f0a1d0d-bba9-39f8-9583-a74fd040bfff | -6.96772 | -42.60258 | 2026-09-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c13dc97-170d-3342-b45b-88b2d4f095eb | -6.52181 | -43.54928 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffb62536-64c2-30dc-8235-da75faa250fe | -7.12745 | -43.07419 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea2c495f-0718-3b11-9a26-d6c573a8826a | -6.98482 | -42.59586 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4d8153d8-8253-37e7-852e-6ef9babb0e86 | -7.02555 | -44.65465 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fa33733b-8f2e-3f0f-8944-5c6b43b9a421 | -7.41121 | -44.73188 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| acdbd39c-3a75-3315-ab46-4cc97012cbb8 | -7.13446 | -42.06511 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f6311665-aeed-3111-8f2f-139eed9f14db | -6.98074 | -42.58887 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba08bebc-c6f1-3cd8-8b28-6e9075ff1af0 | -6.42515 | -43.48737 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb6a7697-ea8d-3e5b-ad87-62402eb6da10 | -7.26173 | -39.18528 | 2026-09-23 03:42:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45ea7eb8-0870-3597-9837-7bfa97b4245d | -6.62134 | -43.75221 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e19dab5b-677e-344e-9e7d-3afc8d9e84b6 | -6.14367 | -43.83733 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3833df2-670c-37fb-b1d0-8a3a87e68105 | -8.55133 | -38.35705 | 2026-09-23 03:42:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fa99f8e5-2c50-3be4-a387-b85d1cd458eb | -6.60533 | -43.74513 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4fa0b85d-e0c1-3acc-965d-14eff89f9a79 | -6.18311 | -45.32204 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9cb23eca-ad2e-35a7-8454-a767d21d20c0 | -5.59443 | -45.37661 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
