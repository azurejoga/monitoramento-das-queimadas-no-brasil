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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 611590a0-021b-352f-86a2-f487110473c2 | -6.95607 | -59.0769 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8be1d4f-da39-3f27-98ec-1652eba90af6 | -8.4589 | -46.99333 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00203448-81e5-3c96-9fed-18295b730d44 | -4.16706 | -42.43736 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d43bd77f-d633-3edc-9bcc-6c4b4b037124 | -6.79642 | -58.66034 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3583ef57-d12f-345d-ac45-b588c5935e8b | -6.86666 | -60.01623 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3ed25de-43e9-3f8d-b62a-eec5b1c7c5b5 | -6.92164 | -59.4332 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 228ffac1-40bd-3c75-b06a-fa805b72abb5 | -6.68565 | -58.7359 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1deb3c3-8044-3060-aa02-724d439125c3 | -6.79929 | -59.58847 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43452e17-da24-35e2-8e88-20a1a7122fec | -6.69314 | -58.72831 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bb36df9-aa4c-3182-8d82-060746ae45e9 | -6.60732 | -58.38468 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08f4b593-60ae-34df-aefd-cf4d966574e5 | -6.80736 | -58.65556 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 173d865a-80b8-3828-bd57-9c39f8166f0a | -6.96023 | -59.05447 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be3d14ae-790c-3f06-934f-01dc5702a9cc | -6.80601 | -58.64036 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10aaf332-9a4a-396b-a128-cf02233f6eb8 | -6.68783 | -58.73596 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2da94c5c-553c-3988-a385-dc01c211f878 | -1.80576 | -47.19672 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c15d1e-6189-31d0-808e-fc09755bd745 | -7.9861 | -45.24118 | 2026-08-23 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8c47198-e8e1-3f6e-ac6f-33fd51ef8ed1 | -6.1835 | -53.52864 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b31e396b-0bc1-33b3-a35e-17584a359c5e | -3.59134 | -54.04218 | 2026-08-23 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d37bb4-47eb-347d-9050-0cb32a875e71 | -6.37462 | -54.96379 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea2c2415-e57d-31b6-9c30-97a78e8c5016 | -6.80819 | -59.68064 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7aeb703-381b-3e96-ae91-cc3d31d0bf79 | -6.95259 | -59.06225 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b38c29-49fe-34c1-a1a6-daaca9a08191 | -5.78265 | -50.19128 | 2026-08-23 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8af1427d-1ff5-343e-84bc-cc98be16ebb6 | -6.67093 | -58.72835 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 19cee5c6-bc01-3adf-84fd-b2884f31da55 | -6.82645 | -59.67014 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9ba6364-55e7-395b-8a2c-f073eca7582f | -6.37546 | -54.95905 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5c14cb7-0fb9-3c19-aad9-4220457a11b1 | -8.09397 | -50.0584 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7325454d-fa77-36bb-9a8f-ae51384b005c | -6.76828 | -59.44996 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bef74491-700c-3af2-a2a2-efa77106eaf5 | -8.48317 | -46.99328 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d673336-a499-33a0-8e5d-72f8e02bfa17 | -7.1733 | -42.74438 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20e7bbee-7b53-3b21-a9f2-16ecee02db03 | -6.79219 | -59.59221 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b2bec5c-63a1-3d0b-b918-b92d4e3cff3d | -6.20027 | -53.53151 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5a8a40f-9dae-32e4-90a2-791aa9d90d3d | -6.78104 | -59.445 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eae6cc6a-44a1-3154-8bc1-a5d1d55a7ffb | -6.78594 | -59.66132 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e408605-38c0-3988-ad31-9b95e47cdfa7 | -6.18065 | -53.52018 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d99d458-aea9-33e0-915d-61df27af0749 | -7.18823 | -42.75816 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ae88c408-7680-39e8-b29b-e383b427e42b | -9.31666 | -47.62985 | 2026-08-23 04:44:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e07fd64b-8bce-3010-aa42-96c0589a6931 | -7.81759 | -42.15426 | 2026-08-23 04:44:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa97f0dd-fc9c-30f5-96af-76b966e8bb01 | -6.67018 | -58.73255 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 03143d1d-073b-3de7-b256-95327076b988 | -8.93448 | -48.54174 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72906abf-68b5-3f52-a1a8-0b032b95048d | -6.89265 | -55.70269 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d23f7416-daa8-3e6c-83fa-88dc42a0d40e | -3.26852 | -49.52413 | 2026-08-23 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 169d1dcb-08a9-3730-814d-4d6e6558e141 | -6.94377 | -59.06855 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d2b3ae8-3fe3-3296-9afe-8c7c7c80e5dd | -6.81322 | -58.65657 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9e5a4231-5248-37a8-8fc7-fedd2fa435f4 | -6.75909 | -58.66611 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b0cb76-e5d1-3676-ab9c-2b5bc6301c45 | -6.84095 | -59.45725 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 19069260-e31b-346f-a7ea-47ace773105d | -6.18682 | -53.5094 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30e821ae-f2d6-327f-ad02-39ec612f6b4a | -5.78042 | -46.10383 | 2026-08-23 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4820111f-4353-30df-99db-cb0169250dee | -8.37802 | -46.47647 | 2026-08-23 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd5b0f71-62b2-3977-9af8-7f68b3e0c8fe | -6.80302 | -58.65725 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b52994ac-a05a-3178-8ec0-c0b734af6154 | -4.93361 | -55.77518 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fea29e9-1f92-357e-96d8-ef11cc6fdbeb | -6.18949 | -55.43124 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c147e1-99c5-3e26-a3aa-ab10119ad56d | -7.03367 | -48.02094 | 2026-08-23 04:44:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82fc5ca0-d76d-3027-b79f-dd42f102c411 | -6.80228 | -58.6614 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 649021b7-1452-33af-8acf-8d9bf4856d68 | -6.38005 | -54.95988 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 398d68df-3250-33b6-ad22-11beac55a3b3 | -6.873 | -60.01752 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fdfcd60-18ca-3fe2-89f7-448ca58c55b1 | -7.05148 | -50.75628 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8323f01e-9d30-33cd-af7c-f2c839277155 | -6.93975 | -59.06469 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d891b48-d2b2-3a51-bcd9-8d72cfc44614 | -6.37922 | -54.96462 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f372f1-52ac-382b-bcf2-52bb0aed8014 | -6.88835 | -59.4076 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fd73ded-f7ca-38d5-9b59-c298857391a6 | -6.38089 | -54.95515 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95f3ffcb-85b7-3b6d-88e7-3c56c1c72e1f | -2.45979 | -49.28665 | 2026-08-23 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29da5aca-3220-3b5d-9d8f-7efa981ca561 | -7.06417 | -44.98553 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92f4fce4-91f5-3007-933e-1a8e5a98f560 | -6.82025 | -59.66885 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7db40f53-80bb-3f2c-897a-86f879ea2bc9 | -6.37796 | -54.94479 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efa33e16-6928-3ca8-80e4-1a0968e48d63 | -6.88657 | -59.41714 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 697369df-dcbd-308d-a8c0-618a74bed6e5 | -6.87486 | -60.01712 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cb7916a-4702-3891-83c6-742b72d2e421 | -6.9441 | -59.07462 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94095dcf-837d-3158-914f-8d6005175d7d | -6.11537 | -59.93454 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bfac2cb-0e48-321b-a3c4-0c341f39f89a | -4.16595 | -42.44443 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40722199-96e1-3fb3-bd54-2c41ba9627ae | -5.8158 | -46.61697 | 2026-08-23 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4d75331-9abe-3563-921a-c16334dad52a | -8.80939 | -46.62131 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85fb0185-9322-3620-86b9-537bfa5ad76c | -6.16952 | -55.57252 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b90a170-7487-37d4-b744-1054693c527f | -4.30735 | -46.41968 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f318fa20-eb22-3005-b85f-0a9e7f4e45aa | -8.92784 | -48.54068 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0f83a3c-fa1a-3714-8367-f5de032e22f4 | -6.49761 | -49.90324 | 2026-08-23 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a388c92-0c04-30dc-a56b-4f374d145d9d | -5.16984 | -45.05835 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6735b337-b2a7-3e52-aa24-db99746841e8 | -6.94816 | -59.07866 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a73ed2e-dd75-3ca1-9268-20540033d961 | -6.11442 | -59.93981 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9c2a3e2-3a49-3fcc-8677-77932ca3141e | -6.67681 | -58.72948 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d3bdda57-3b63-3de1-b298-dd5a9764cf4a | -6.66126 | -58.8018 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20212d31-e466-36e3-83e7-2674d2d41f98 | -7.37221 | -55.6743 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed2d164c-456b-3053-a591-4cf9d9f1449e | -3.26791 | -49.52796 | 2026-08-23 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88bb12d5-1e1c-3bc8-be60-814f4d937f9f | -6.65209 | -58.79977 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbd7a7f2-3113-314d-9d3c-f24bffd7bdc1 | -8.93172 | -48.53772 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c70f917d-1670-3ba6-ba11-89e248b8d7a0 | -2.56998 | -47.24692 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3f575d7-b4bc-3f80-8c57-6a04a6a3bb0f | -1.82431 | -47.89032 | 2026-08-23 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9386f4c7-38cf-35c5-be73-2c17e61166ec | -6.88952 | -59.4068 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9b0d145-dfa9-3e79-8c2f-44d1babee341 | -5.95299 | -52.12958 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c300ed2-98de-358a-8e45-f077d3a79ba0 | -6.79859 | -59.41885 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a200c29b-7a11-304e-b36c-f97179c7c0da | -7.15023 | -42.78683 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd372e81-29a3-35f9-841d-428907acf960 | -6.19101 | -53.51013 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47be12a-4f67-33d1-9e0d-a7162256264e | -6.89689 | -55.69899 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0f8aaa36-a7bc-3650-8171-20bf073b91df | -6.75984 | -58.66195 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81935945-4967-3600-914d-0fa3c0c08dca | -6.17525 | -55.56823 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a9bc16-a4a2-360c-bda5-b96d102f0820 | -7.29778 | -47.43736 | 2026-08-23 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 783140cb-e322-3fd9-a5e3-18cce4a1011a | -7.73449 | -46.14437 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c8f902c-39d5-33df-a88d-e5d4ffc44ccb | -4.53754 | -55.51571 | 2026-08-23 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3f17e70-e2f7-38df-a2e1-054c03f61170 | -6.55975 | -55.09678 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28d05c0d-76de-3d37-95de-0d9715d2363a | -9.44988 | -40.32615 | 2026-08-23 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 378df29f-58f6-3259-baca-819ff4906c40 | -6.55274 | -55.09739 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README29.md)
