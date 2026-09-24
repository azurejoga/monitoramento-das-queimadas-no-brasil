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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a69f4a-86ba-3644-981e-94bc19926df0 | -2.89408 | -54.0881 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e2d8e438-5365-39ff-8abc-f2da3ad9c1f3 | -3.55183 | -59.94884 | 2026-09-24 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5efca35e-cefa-3ef7-bbd5-d59a18926296 | -3.8192 | -58.89034 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60edb537-1160-33de-b3c2-91d3c2cbbaac | -1.2796 | -57.0341 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0375ab34-bdf5-3bea-a12e-39ef26d60fb5 | -5.37071 | -56.05771 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74c08ae3-e376-34f9-b173-2a6a84a3ad76 | -1.92268 | -58.26141 | 2026-09-24 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65546fe2-2a00-3f73-ab7a-68d0d81ec571 | -3.60697 | -60.57508 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38e1dda9-063b-3750-a6e6-cdac6927e5a2 | -5.4078 | -60.21567 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd4866b1-8aae-36ac-986b-87c2f0b137bd | -3.68408 | -60.57807 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e6c3351-d76c-38e8-83da-7f579fb6b552 | -3.08077 | -60.99664 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff30e788-5e9c-3b64-8da5-c24123e5e43d | -3.49726 | -59.17511 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d4ba2c0-b3df-303f-9e54-d9864aea17d9 | -1.88559 | -55.52427 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdc19a78-d1ea-388e-b5f3-8e268823f76d | -1.19668 | -54.14038 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b583809-e88f-327b-b7eb-ff5f78594a36 | -5.14494 | -60.31794 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba37403b-5eb5-3a01-8e25-f97f12c77133 | -4.25787 | -60.00801 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d01af3a-f7e7-3e63-9f36-b4e5b9957d7f | -1.82322 | -55.33591 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d385b2a-1586-3706-b4c1-7d5ae37a52bd | -4.72213 | -55.98673 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67f4fe02-e3f3-3772-b1ea-fba9c7d7b1c2 | -3.75338 | -59.30946 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 948f3087-d9fb-3517-91c6-0d1bbcf064b0 | -3.91278 | -59.66401 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34c3e638-0c98-3b6c-ac59-ae69f5de29b6 | -1.21623 | -54.55107 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33e24a8a-460b-33fd-9762-a22081d492c9 | -5.76779 | -56.52033 | 2026-09-24 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fbadd60-6cc2-391a-8377-8b6950587adf | -3.68645 | -60.56205 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc8a72e0-f6b7-32af-ba5f-e14b58453886 | -3.68337 | -60.55334 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c34f6afd-7dd4-32d2-a114-7f3fd44039c2 | -3.72073 | -54.20657 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9757fef0-4b30-3c7b-996d-7c0b5ef4d6f5 | -3.1661 | -60.09419 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df19cf6e-955b-3f8e-8d08-8d33a880ca09 | -2.70934 | -57.50407 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2681e1d0-27d9-37ea-81c0-56757eab86ae | -3.60636 | -60.57906 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cc63450-78a1-37d0-85be-2f25b53bf444 | -3.16865 | -60.10129 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6b161e0-3468-3d1f-8ee8-895c569e714e | -5.42323 | -60.25316 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a96602a6-313e-369b-87ee-6764fae6cf61 | -3.77024 | -60.72722 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02568611-f81c-3970-b9e4-f2403eddabb1 | -3.1593 | -54.59944 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fa02fb6e-dbaf-3873-8d8c-263175da1963 | -3.48496 | -59.19333 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 280a9a51-92f1-3886-b64f-3b05059112fc | -5.11254 | -60.2591 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4357006-2327-3a2a-a6e5-fbd00cf0c324 | -3.67981 | -60.5774 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce125d5-d8bd-3503-8882-dd4d41010a64 | -3.6823 | -60.59007 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc2c4128-dea6-3c5e-abbb-87e152f966c3 | -3.73253 | -59.42006 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c22aec65-c8a8-37fb-9a31-a8973699f773 | -2.93298 | -56.58227 | 2026-09-24 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edacff7c-43b1-32a7-a5f4-2e060763b4d2 | -2.89971 | -54.09448 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 405ae87c-0f60-37a2-89b6-9c51a97e29da | -2.71453 | -57.50488 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 928e42ae-5218-320f-aba6-3c1adc357693 | -3.90639 | -60.59629 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b6549ba-d216-39fe-bd71-2c8732de424a | -3.11493 | -60.68195 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d37bc9c4-21ca-32a4-9464-6a22f7b90ab0 | -3.15856 | -54.60454 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 62e351a2-e95d-3f9b-b8b9-74aa50e1d059 | -1.21547 | -54.55618 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb7833e5-4fef-306f-a503-4abafed59ee5 | -2.64552 | -54.68944 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0af874bd-f2c8-3803-87ef-b8ab52460cf4 | -2.71362 | -57.51115 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 193ae7b0-1a86-3aa8-ab95-fc268cfdd1f6 | -3.80959 | -58.88893 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f9bfd19-bb23-39bc-819f-79a91a8cec43 | -3.83413 | -59.36413 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ff8d908-485c-3542-a7c8-1d0bcd07b84d | -3.95843 | -59.34943 | 2026-09-24 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| faa94000-c120-38b7-9b24-8e4751ab41be | -1.19584 | -54.14594 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bfa0869-3f86-38eb-9e8a-a1fa4159a69f | -4.26234 | -60.00871 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99c859b4-5285-3146-9931-3c662f604d3a | -1.83252 | -55.71825 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d7497abe-9943-3809-8f51-12a7b2d5554b | -2.47053 | -57.91347 | 2026-09-24 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20536957-4d10-36bf-9b46-08cb57d92a31 | -3.16986 | -60.09914 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 557b316b-c18b-39ab-a1fb-5b3bbf5431e0 | -3.4889 | -59.19899 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1908feae-1ed5-3cab-9667-aa7821b43308 | -2.83567 | -60.22805 | 2026-09-24 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba7b747-7be1-3ed7-a526-af69a48921eb | -2.9462 | -57.78439 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 309f9d32-848d-3a61-a0e8-a13e623aa657 | -1.27387 | -57.03648 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fad40040-502c-32a9-bfc8-5e846a7e33af | -3.1706 | -60.65487 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc73b566-3a4b-31a6-97ff-90bbe71c4483 | -2.89892 | -54.09996 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| aa009a89-c0a9-3661-9c9e-6d67383da519 | -3.68824 | -60.54997 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5361d3e-5b00-3299-8965-4477f1ab2682 | -3.72103 | -54.2006 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e5a5271-bd09-3e96-b185-038ea78dfbc1 | -4.47077 | -54.96909 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f64a3efe-2971-3853-b9d4-ba7987b2c7cf | -2.94109 | -57.7836 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0a1377a-ecfd-33c1-9c2e-f6a3f4c34ce2 | -4.71622 | -55.98582 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37514328-2056-3382-8b6a-e516ac5715d2 | -5.83617 | -53.85196 | 2026-09-24 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc5c282-e54b-3de1-9acc-f68a25627c04 | -3.68112 | -60.59805 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 02c742a8-89de-376f-abd1-faa633eea2ca | -5.11191 | -60.26352 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6dcef21a-e657-3a4d-913c-9ceef94a1887 | -3.96704 | -59.35574 | 2026-09-24 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dbc5ce4-814c-3b11-972b-b443d07aef96 | -2.88759 | -54.08707 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01581d94-7512-3285-a517-a6bc7d34373c | -4.06484 | -56.22425 | 2026-09-24 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22790fd2-e508-33da-8b7c-e8125ce11f4d | -3.23182 | -54.3239 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe2242d3-41ca-3025-b7d1-4f6e064985f3 | -5.22022 | -60.05473 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 387fc215-e6f4-35eb-a1da-be8c2f986d1d | -3.17481 | -60.65549 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6990c0c-09b1-37ba-b2ca-6771d495bb61 | -1.62608 | -54.91697 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 325718f5-7f5c-38c2-af42-9f48ae06275a | -5.81931 | -57.74176 | 2026-09-24 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f29c00-8fc3-33ca-8e60-30af66626e3e | -3.90698 | -60.59227 | 2026-09-24 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b3fb5d4-1fe6-3d5c-8743-de4bc4f4f672 | -1.27533 | -57.02674 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4b683b-c5d7-3da3-9344-93cc18de62d6 | -3.83527 | -59.38912 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e6093e6-5ed5-3823-bc1a-e40f1cc0ff8a | -3.1817 | -61.10101 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d165a0fb-1563-3bbc-97dd-28a5cb36424b | -4.0307 | -59.84791 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff885cc-05bb-3bad-ab62-f63a0691f99c | -3.71423 | -54.20543 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ea4847a-ee59-322e-8df1-01f46cdd8b29 | -1.22202 | -54.55749 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 19d176c4-dbde-3844-91f8-b303b963a537 | -4.06384 | -56.22662 | 2026-09-24 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1513071e-b42d-3383-b26c-5639e44f2928 | -3.67863 | -60.5854 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98debda0-6062-39c1-b756-0467f5e59681 | -1.62003 | -54.91592 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d5fbf9-81cf-3f4c-a84b-9721dc3cc889 | -5.24653 | -60.17162 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ce24f3c-5b20-334a-b93d-ead450eb8178 | -3.89416 | -60.59031 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba6657c-b498-3494-94cf-48a44e2ac1d6 | -4.53361 | -54.97884 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0bb6af8-0dd0-393f-9fea-0412aad74ead | -3.68277 | -60.55738 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bd48475-22ee-3299-a51f-b4993498a9fd | -3.70731 | -54.20345 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c504db0-1061-3f5d-91ec-9ba19ac25d3e | -1.92361 | -58.26672 | 2026-09-24 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04ccfb26-c597-3ba9-a70e-46713a2adcfc | -3.70943 | -54.19267 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1657356-d7ef-31fe-9007-461bff11fd4d | -3.68218 | -60.56141 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f0b165a-ef3e-3693-855a-b87498e1b5f5 | -1.27484 | -57.02999 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 690dc6c2-b40d-39be-8426-aa8bd5ddb910 | -5.37133 | -56.05333 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32fecce2-7d01-3953-a5d8-6eb2882c1542 | -3.67922 | -60.58141 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ee3b345-d415-392c-8ba5-14a48f42979a | -4.09217 | -62.09662 | 2026-09-24 05:48:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e61be987-535a-3dc5-890a-77c328a4f536 | -2.89976 | -54.0945 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a6abf912-dd14-314b-b7ab-959080b526b8 | -4.06727 | -59.86412 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b00808e-3ac1-3deb-bc55-971b108df522 | -3.72153 | -54.20108 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README82.md)
