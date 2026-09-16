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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6f5c191-eccf-34e0-98fb-fa55449fa6cd | -5.24098 | -59.98273 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bd1abef-9b9d-33f2-ae68-c021cecb7db2 | -6.09165 | -57.69854 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9decff3-8e7c-36c0-9006-95aaf94cac62 | -3.37257 | -61.33547 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41ebb71c-c7d6-340b-a6b4-3631bf0bc559 | -3.88268 | -58.7447 | 2026-09-16 05:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59ee0ce3-ca29-324f-a2da-7b56f1233923 | -3.70845 | -60.61966 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d3ab4fb-1c2c-319c-bd30-3f3d19e82d63 | -3.4266 | -58.22852 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 363766e4-c8ee-34a6-a275-181697b3bdf1 | -6.107 | -57.62871 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25322e27-6400-3adf-80df-c954064d638b | 4.75088 | -60.56801 | 2026-09-16 05:53:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00f8e61e-e9b7-3af5-8c34-5ccc459e13d0 | -6.44464 | -60.0136 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9610b64b-a301-3c8b-b288-c5741a471e2b | -6.44534 | -60.00879 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26c9f3b3-01f4-3b17-b591-5ce79749f9ae | -5.75589 | -57.5946 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b0d828e-5e96-3e15-9562-38e8366af69a | -6.13121 | -59.88294 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a41445c1-b95e-3f33-95a3-4d761939b9e6 | 3.14312 | -60.41598 | 2026-09-16 05:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13d9e50c-79ec-37b6-9519-dfa153cd107e | -6.0236 | -57.77167 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e4c9bb6-ca67-35b6-9dd3-c51bde6012e4 | -6.10602 | -57.63563 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e6573a5-7a5d-3337-a0d7-735d31a3df9f | -4.37587 | -55.02774 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9b38388-bd24-38b4-a8f6-584568f15991 | -3.73733 | -55.94857 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a37bb1a-cb9f-3d8f-8af6-0848319ff399 | -3.7499 | -61.75828 | 2026-09-16 05:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06a5b579-9cbb-312c-ab65-c7834680f9a4 | -3.53617 | -59.07102 | 2026-09-16 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 947cbe3c-84dc-3e27-8940-379133d35c38 | -6.12656 | -59.88223 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9954caba-7149-3220-a585-2bafcf244b33 | -6.75231 | -58.8088 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c62d83e8-ec66-3198-b62f-c2f5b388214b | -5.75197 | -57.59567 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebf3e2c2-fb74-33a9-961b-0a1959feeb1d | -3.70419 | -60.61903 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64796c38-c7cf-3e26-ae1c-5c6ae50e2f91 | -6.34993 | -55.56617 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48cd5145-c395-3cf7-bc12-1ed3dc3fbb26 | -6.32938 | -60.0001 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b61659e-9cf2-36b3-a84e-f7fcb1652ebd | -3.5895 | -58.54632 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fa8adee-9da1-36a0-ac84-ea35aadf4d1d | -6.33119 | -60.02008 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec3dc18e-52cd-34bb-b557-b3c4442bebf8 | -3.22497 | -61.2109 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c197a1ae-b640-3a8f-80c4-f8d6f95f1592 | -3.04887 | -61.27504 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87c3a0f8-85d9-3bf0-87b9-8cab1d94dcde | -6.12513 | -59.89204 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc8ceab5-73fd-36da-b817-dbb209cbb8da | -6.34977 | -62.69701 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9e125a6-ef27-3751-868c-b4c3825068ea | -3.44334 | -58.00957 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b92f5d5d-3431-3438-acfa-16af7351e621 | -6.77206 | -58.80724 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00346830-bc0e-31f1-9cb8-94c93adf5439 | -6.79479 | -58.79258 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cae83b14-5eb0-3067-8572-4339f77b9f20 | -5.48622 | -60.12643 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ae391fb-9666-3f68-945b-f3d53e06ad2d | -5.46283 | -60.22039 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d7c0d87-e912-3607-b987-d63a9eacc360 | -6.3287 | -62.679 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9eddf4c2-b590-39f3-9af9-34d457a9bfc1 | -6.43177 | -55.60557 | 2026-09-16 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f768ef2-083f-346c-bd6a-6f540e55dc80 | -3.18561 | -61.11235 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cd5d6bd-becd-3829-bcdd-663d10d76b31 | -6.75138 | -58.80732 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7a26ee2-9e4d-36d9-b6c0-91646f8fbfa4 | -3.42532 | -58.23714 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbac5796-a995-398d-bb73-3e4476d5e3e9 | -6.3459 | -62.69642 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30106064-f388-3af3-8c6c-f9bcb8a2b7c9 | -6.28802 | -59.92496 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a71f3a1-a89d-3756-b38e-a4796d287bcf | -6.75695 | -58.81244 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbb78bb7-6588-3692-bb6d-0cb2a0612b69 | -6.28338 | -59.92422 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2361f08c-9302-3382-a46c-92f903c1b0d9 | -3.10851 | -61.1004 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52b0269-d982-3e95-9b1d-97115dd3c0b1 | -4.72361 | -55.7338 | 2026-09-16 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b59337f-aa09-3f0f-a461-dd7414e506de | -3.42575 | -58.23426 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 065a0488-1223-35f2-907a-5037f4e24eca | -3.17597 | -60.08949 | 2026-09-16 05:53:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d66732b-2ff8-3c47-8316-8aa30c1bd970 | -6.32798 | -62.68385 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9ffaca96-e00f-3e47-af04-96391dce3818 | -6.43627 | -55.60556 | 2026-09-16 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c5e707b-2b43-368f-beef-d1ad062080ce | -3.17283 | -61.11781 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea7e6c93-ab46-3d9b-8a84-098b42289d65 | -3.7531 | -61.76395 | 2026-09-16 05:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42254376-70b8-34ba-b285-24c091447c65 | -3.84402 | -59.33146 | 2026-09-16 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bae16d4d-d2bf-332c-ba6d-e653af3bfcfa | -3.73709 | -55.94338 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9386697-172a-3e6b-9608-fdebef69b4e6 | -6.34855 | -55.56411 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdc04f49-33df-3413-8b34-46b89cf816ea | -6.8072 | -59.17047 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20fbdd5d-ce8c-3d6e-9d18-2073c2e19ffc | -6.13049 | -59.88785 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 963e1f57-09fe-3533-9300-59123279fa29 | -6.33501 | -62.68985 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe589e49-e438-362f-a496-b1ac15a47862 | -6.34203 | -62.69584 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d259bc9-c994-3479-a31b-8f433afadaf1 | -3.37798 | -59.53036 | 2026-09-16 05:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66813dea-7d84-3897-9e78-891eccb463dd | -3.73559 | -61.7457 | 2026-09-16 05:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4984084b-7b20-3123-9d6b-2f1ce45dd895 | -4.40666 | -55.07944 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8324633-27cb-351d-b651-a142cf2ad1af | -6.34921 | -55.55921 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d07d6c1-fcd0-3f08-bfd2-596afd7a9146 | -3.32431 | -59.45025 | 2026-09-16 05:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22f3c96d-9fbf-32fc-8e2f-0112e1518459 | -6.31894 | -59.97414 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e23938d9-9ee9-327f-97db-861e1f30febe | -6.77247 | -58.80428 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb7c93d4-7a5c-3148-8721-2ce4dd3b1e9f | -6.32727 | -62.68869 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b9b612c-8f88-3d2d-b0ce-2a63fff8a7fb | -6.31501 | -59.96851 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200a1e8f-169a-3d6a-a289-b20588aab54b | -3.12214 | -61.41535 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49d34e76-c71a-3e3f-a2c9-07badd498927 | -4.37515 | -55.03271 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 853f2b53-d651-3ba5-bba1-18eaca7892b1 | -3.18206 | -61.10809 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 226062e2-f04e-37ba-baaf-3b4de20aa066 | -3.42116 | -58.23063 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a439da-e392-38b8-aa76-de8f7c5808d5 | -3.73214 | -55.94322 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13fcd888-db76-313a-a44c-9e97f0826904 | -6.33186 | -62.68443 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| eec00eb9-6866-3d49-adff-95bd0d86c82c | -4.72294 | -55.73835 | 2026-09-16 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c50cb917-d28b-3354-aebf-0bc1a92f930e | -6.71101 | -58.80867 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89416817-69f4-3465-a72a-2315536e1554 | -6.37515 | -55.83212 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f426132b-4f1f-3c8d-960d-93f5a5606a6b | -6.10651 | -57.63219 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cf799ef-fa57-3f5d-80ea-a2b9f9d6a66b | -6.71607 | -58.8094 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3189393-d4f4-3cf4-a481-658e75cee9a7 | -6.71731 | -58.80069 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2aa355-ac06-3158-b098-bb32f2ad0e1e | -6.80826 | -59.17193 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 47b29a95-fdf2-3639-84cd-e94a3e5a75de | -3.04536 | -61.2709 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4812ef74-c808-38db-be3b-ddf7ebc99786 | -3.59031 | -58.54085 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a201a422-099d-36eb-be1a-5c493a2d4720 | 4.75021 | -60.56616 | 2026-09-16 05:53:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2171ca6-8ecc-3711-97fe-b969001de997 | -6.3505 | -62.69216 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c166b5d0-6ba9-3a49-bbf8-1bf871f3f817 | -3.32493 | -59.44934 | 2026-09-16 05:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a3a61e2-7fb4-3d22-a95b-c918a1281a0c | -3.84328 | -59.33638 | 2026-09-16 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d45fc835-02ea-3096-931c-a3386191a0b3 | -6.32868 | -60.0049 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffa92171-2077-3e4a-bad1-2b58437e76a1 | -3.12254 | -61.25362 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a447ca-f470-39b1-8118-e8416f20f28f | -3.18983 | -60.50577 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5692e6ae-f8c3-3350-8d6d-53f118433c27 | -3.38089 | -61.30763 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7896ac-3e58-3a7a-b1dc-83b1d9b01aea | -6.767 | -58.80645 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4820cd7e-980d-3ab6-98c6-19a49499167e | -4.42887 | -55.78913 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fc2ed2-7415-303f-9356-df5ceb71f04f | -5.75245 | -57.5922 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcbc7f7d-1a07-3d91-86c2-c54b8e74a6f5 | -6.77835 | -58.79914 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 251c2b0b-a401-386c-a838-981036e4bab2 | -3.69992 | -60.61839 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17fe306f-ab5e-321b-863c-781fd23afbb8 | -3.18152 | -61.11174 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b28ecf97-9f7c-3d39-b2a2-41283513c630 | -6.33189 | -60.0153 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3e39e19-0572-31b3-bf42-41d35123fe33 | -3.70359 | -60.62303 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README63.md)
