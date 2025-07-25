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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e5d5f34-870f-3079-9bde-d98626700cd2 | -10.61947 | -44.76829 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9beb0bc7-8c5f-3115-becf-7fca0fe2a201 | -14.65362 | -46.83245 | 2025-07-25 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 651e87e0-3c84-3c25-8fab-9dd3c766da63 | -10.5045 | -44.87815 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 522125ba-5178-3e6b-908e-d26ef4e910b3 | -14.94918 | -46.97415 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf139c2b-280e-3004-b5f5-931016a8431b | -9.23267 | -47.55428 | 2025-07-25 04:46:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 658c2d59-d01e-30e9-a124-a1831da9baf8 | -14.95724 | -46.97967 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea58e48b-2585-32f4-a907-b34d8bab3015 | -8.13223 | -49.58811 | 2025-07-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d06bd47-e7bb-3097-9247-c7a27c7817ba | -14.9473 | -46.9889 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4259050a-1d9e-305a-9623-819514c1d0d7 | -8.89148 | -45.57961 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07f69130-c141-3333-afa3-5ec35b4e36d3 | -8.89084 | -45.57207 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 87c6e070-0446-3f7c-bc63-5e7a50b762c4 | -10.04781 | -59.10076 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07a5aa64-f6ad-39f0-99e2-3a9767251922 | -9.00582 | -45.33595 | 2025-07-25 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c837d2-c242-30c7-8a13-2c19241fc465 | -9.07687 | -46.63392 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08bc7c59-8d3e-33a6-ba94-4e0c2d21027d | -12.4264 | -45.38485 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bd69efa-8bfd-3db4-83c9-2d5565853fc1 | -12.25163 | -44.78352 | 2025-07-25 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ee77e77-65d7-3242-a760-d74e6b4a4733 | -9.11871 | -47.64654 | 2025-07-25 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcd41c55-73f2-3b38-9323-347b941fb2e1 | -10.04321 | -59.09992 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87df18dc-9494-301e-9198-7f53dda0192e | -11.44673 | -45.12926 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 990c2967-33c8-30a4-860d-fe5aecd04723 | -8.11984 | -50.46392 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc92d88-9f69-355a-abcd-e6c43513c1e7 | -8.89103 | -45.60132 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 905d5ad3-65ff-3f05-9202-ba1c0b6d69b4 | -9.07737 | -46.63038 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 657effbd-da13-3c58-9782-ec5463cbe1c5 | -8.12039 | -50.46035 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634f3c8f-f027-32d8-89a4-230fd395c25c | -11.94092 | -58.76176 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3e2f350-ffa2-3347-9f52-33eddfc40c72 | -12.43233 | -45.37564 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65603c09-f8e6-3874-a088-10c959701e7e | -13.71612 | -45.68638 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4673f6b4-a36e-30b2-8523-8d9358f227f2 | -13.71673 | -45.68147 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6b737f2-a349-3957-b73f-72d24f5a4130 | -8.84163 | -45.6071 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb30417a-160c-3a59-ba63-c68df1fe47fb | -13.70929 | -45.67356 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16ded36a-77bc-3811-a65d-2fbe08aeb7a8 | -12.58022 | -56.981 | 2025-07-25 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76aa1f17-06bc-3fef-a197-dd0524c39aa2 | -8.8934 | -45.58498 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d48b4a2-6a28-370e-93f7-3525b0eed9dc | -9.03907 | -61.23109 | 2025-07-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fbd18f7-32cb-3c0c-9076-f0e05f2cb438 | -8.84335 | -45.59497 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d30a128b-cbe0-37b2-893d-22eae2416ff8 | -14.95293 | -46.97915 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 122318a0-c5ae-3e0e-9acc-56781bee0861 | -12.77417 | -48.81506 | 2025-07-25 04:46:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f4550cd-76a3-3bd4-8ef1-e720724f099f | -13.64598 | -46.81727 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ae16629-21bc-3dec-a9a5-bc27f3b8d3e4 | -11.44145 | -45.13352 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6970b789-a3cf-3336-9283-32ea4094b18f | -9.2569 | -50.04148 | 2025-07-25 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 889a3d6d-9085-3b0f-8f38-bfa0e6cc341e | -13.71659 | -45.68945 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e3ca2bc-18c5-39f3-be60-af0134ab7f5e | -15.58783 | -49.85109 | 2025-07-25 04:46:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fa80ac86-15df-31d8-af07-5dd277d675e1 | -9.42713 | -44.73645 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4011fab8-0ce5-37c0-aa7c-ddbe914aad6a | -9.07233 | -46.63683 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d916487-83fb-326f-83c7-f9a8fb33aae7 | -8.89526 | -45.58428 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41a345df-c171-3c2f-aa0f-aebc29c4dc21 | -12.69609 | -46.99766 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84cab99a-e34c-36f5-80f8-16a405439d66 | -13.72074 | -45.68698 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b74972aa-1659-3c15-bb14-670939183c7e | -15.82589 | -45.77888 | 2025-07-25 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9af75073-1488-3628-95da-1fc7270f819d | -10.42212 | -47.19159 | 2025-07-25 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 09186061-b9d1-3e70-883b-581c066f56f2 | -14.94625 | -46.97788 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c2ca0f1-8d22-3353-917e-dab4fac7f9fc | -10.41814 | -47.19101 | 2025-07-25 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 42df67c9-4eec-30a2-afcb-7721b3fc7b40 | -9.58943 | -46.32626 | 2025-07-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c56b17b-6378-3015-b27e-7d6f7979f52e | -8.89469 | -45.58842 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ba3c101-84f4-3daf-b3cb-d938c2277308 | -14.93496 | -46.98262 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05bce8df-d27d-3aad-9044-48a3efa2b5c0 | -10.36464 | -57.49966 | 2025-07-25 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 685b2440-e675-30ae-b7f5-c9395b1fb9df | -8.893 | -45.60064 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d15735f8-1b49-3ddb-8e00-bc137c6a9580 | -9.59918 | -43.8757 | 2025-07-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d4974f22-36b4-392f-bc49-3dd740241d60 | -9.73894 | -65.11383 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9960483b-3021-3f88-97b2-4fde1059cbf1 | -11.32015 | -55.21306 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9448904-10e9-38b4-b6be-747c65120e91 | -11.38429 | -48.18988 | 2025-07-25 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d3010a8-973f-3190-a534-28c6e63a98b3 | -12.69822 | -46.9817 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f21aa7-94c3-3ee3-b74c-db95f7619d56 | -8.06348 | -49.7186 | 2025-07-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b11ea525-f022-37e8-9f9f-2dac1b5462a5 | -12.69769 | -46.9857 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 509b0260-bb86-35bf-aa62-db0dfbb3af68 | -8.93179 | -47.34109 | 2025-07-25 04:46:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e1ee5c3-1c22-3a0a-89f5-b3948653d47f | -11.31889 | -55.21544 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fad1553-9e88-30b9-8f98-6a9a0557e246 | -15.33941 | -49.42324 | 2025-07-25 04:46:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 438d3c65-2ac0-3517-a93a-c0f820955918 | -9.11491 | -47.64598 | 2025-07-25 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f24adb6e-05f5-3662-80b7-cbaafc40faf3 | -10.63007 | -55.30691 | 2025-07-25 04:46:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd08919-b1b8-39bd-a553-cd2290093944 | -12.23131 | -44.63271 | 2025-07-25 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d134c9bd-901b-3cb1-acc6-3799858eec07 | -13.71594 | -45.69432 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 116c476a-3f53-3913-a4fc-aebb51ce2dbd | -10.8741 | -55.19125 | 2025-07-25 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d5f9b65-93d2-3843-bd99-31fb3ee37000 | -9.13546 | -49.66744 | 2025-07-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d454d3de-0caf-33bc-ad36-178371d06f7d | -11.45667 | -45.12555 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0485c520-7187-36c5-be69-d1d2bfe4348f | -13.71326 | -45.67907 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89b31142-75ae-3d3c-a6d5-1189d1db0170 | -8.88866 | -45.60013 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e3afa9a-3f55-31f4-985a-181621853846 | -8.85461 | -45.60891 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d82ce12-d276-3c53-afb0-ba4355deace1 | -10.42611 | -47.19214 | 2025-07-25 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 643ba144-221e-3b89-8431-c552d51b5649 | -9.4672 | -48.51524 | 2025-07-25 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9711a7-37be-3a8f-a40c-d2fe8d174327 | -11.45795 | -45.11579 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5888fe7a-c288-3a34-b486-9617cd707fc1 | -12.7361 | -46.98439 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7b34099-d094-3f48-8ad8-52ff0ee2720c | -12.04609 | -45.43523 | 2025-07-25 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc44ff89-4688-360b-9eed-ee04568cfe99 | -11.46663 | -45.12169 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ab64546e-bbf0-3331-a799-04c5e0109bc3 | -12.49716 | -55.74052 | 2025-07-25 04:46:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91e23a1f-3c67-3a5b-ad14-6130806b5c2c | -11.78168 | -47.32384 | 2025-07-25 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 285354be-7531-3265-b0a3-472e7cb63059 | -13.69878 | -45.68204 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 701ccdbb-bc78-3b3c-ac5d-8debb0a9a4a9 | -10.61041 | -45.23893 | 2025-07-25 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7c1edabd-7825-30e3-94c2-8b3325b32289 | -14.95679 | -46.98324 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c04249-9102-3dac-8e3c-a50668264ae5 | -8.0703 | -49.71962 | 2025-07-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88e4c231-1d95-32a7-acf4-9a70bccc7e8b | -10.41741 | -47.19618 | 2025-07-25 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c18a6ef-ce1e-3c5d-bf04-21bcb55ce14d | -11.78522 | -47.32795 | 2025-07-25 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 457c2ddc-969a-3727-9f0c-674067ace85d | -13.64706 | -45.71927 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6786dcab-ebb6-3a26-8d71-5df52da70011 | -10.61104 | -45.2343 | 2025-07-25 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8292b6c5-4a5d-31c5-a276-e4f4b25396f0 | -14.17065 | -45.35192 | 2025-07-25 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a524a1a1-0040-3dfb-b134-1fab752e9c14 | -12.73141 | -46.98764 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25541661-8dc4-3888-bbc4-6204d9a92168 | -14.93669 | -46.98386 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99eee4b1-8321-3e9b-be9d-9dfa2bb27a12 | -13.09799 | -52.14016 | 2025-07-25 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2e05883-f49e-34a3-9af8-88fa83758744 | -11.67763 | -58.48798 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c5ccab3-8233-38b5-bb9b-c291e05dcf07 | -11.45602 | -45.13043 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a3b37fcf-6490-305f-a793-5b2d810fbf32 | -9.00141 | -45.33529 | 2025-07-25 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7b8f26-89f1-3de3-a5ba-29d777940332 | -9.20442 | -59.68354 | 2025-07-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92922721-a449-338e-9e98-cb7ac8ac9a98 | -10.04694 | -59.10558 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb5bb496-dc3b-35d5-8222-85e15f89f8a1 | -13.71391 | -45.67417 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 341b47d6-bcaf-3d5b-a052-ba66d54e6508 | -14.30652 | -43.79547 | 2025-07-25 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README24.md)
