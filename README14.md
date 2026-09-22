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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bf2703e-65c8-365d-9132-a15335508055 | -5.8041 | -57.7332 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 148fd7f1-52d6-3979-897f-b332a1eabd5c | -7.3415 | -55.6119 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea0023dd-0c9f-317e-8665-1e8f0e9b8874 | -3.5062 | -59.580399 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdd36cd9-bf92-35a1-87c7-90a8899b4ad7 | -6.3513 | -57.779099 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6af18fc3-09f2-3010-9f60-6261956556f3 | -6.704 | -58.998299 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5806b865-5d44-3d31-9b01-9f631cfe8c4c | -3.3079 | -57.871201 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04956019-afec-33a3-ad3d-722ef94443d0 | -4.4833 | -55.483299 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecee61d6-0fe0-3f92-a026-5d624ed36fa3 | -3.8224 | -58.891998 | 2026-09-22 01:19:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a62abcd5-d687-31b3-92c2-8ea6e440a29d | -5.9789 | -57.775101 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c62216-9cb2-3b8f-8fd9-cedd978d2112 | -6.0964 | -57.6591 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0f8709-efc5-3dc0-84b9-97b3013f5992 | -13.2821 | -51.760399 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a17d3ecc-0ad7-3f06-9786-0afe11a1d692 | -3.3601 | -61.284599 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60540e56-25f8-3d52-ab37-be395271fabe | -3.6853 | -60.586899 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44c27b4b-2dde-3cf3-9f8d-6856c5db4380 | -8.261 | -55.308399 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc5983b-4bd5-37d6-8c30-1d9a7d006bd5 | -5.937 | -59.9748 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d612ef8-a8a4-37d0-b75f-46efeea57fc4 | -6.5281 | -55.359299 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2294b350-567a-3722-b9e7-efb2d724d139 | -7.3278 | -55.597698 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c3c82a-0ef2-36e4-a249-d601e88191ab | -3.5989 | -59.445 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65a0cab5-f483-389c-b952-a96960888233 | -5.9402 | -59.988701 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac79dcf-e4af-36f2-b2f8-63a7507abc5e | -12.1547 | -47.416801 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10ba859b-5590-35d9-b56c-46a39b34e2c9 | -6.1634 | -57.725601 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 209146ad-d900-353f-97cf-124423d7c659 | -3.3716 | -61.2896 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41efe115-3f2a-3ed2-9ee6-1999c6114cf2 | -2.4163 | -57.896702 | 2026-09-22 01:19:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06c7e3d4-87d1-3b0b-9e4b-b181e200d75d | -6.3446 | -57.8839 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e783c8ca-59f3-3ae7-af9d-2ab43099bb7d | -6.0997 | -57.628502 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8994c34a-17b3-3218-b3ca-4fd3535aa0e1 | -9.6712 | -54.334 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca5b19ee-78cf-38b6-b135-7136b03857fe | -4.0734 | -55.319 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c709d436-cf75-3368-abaf-a0bea29531f6 | -7.5729 | -57.662201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acec78e1-3ad3-3632-be48-e5c44246594f | 1.0808 | -60.671001 | 2026-09-22 01:19:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 62e52775-8b47-3ba4-a506-7c7fbc37ea0e | -4.0789 | -56.220699 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 871ab6d7-8aae-3da6-a07c-b65e56443871 | -6.3158 | -59.9636 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72a292c1-eac8-37fa-8a35-5b6ffcf308bd | -10.4677 | -51.304199 | 2026-09-22 01:19:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f030fcad-77c0-31bb-a058-a1c39b978954 | -10.455 | -51.3358 | 2026-09-22 01:19:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f59c03be-f0f6-318e-b629-b70ec46ef589 | -3.759 | -59.4235 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a35363e5-4878-33dc-ad29-c0b448af44ae | -5.983 | -55.367802 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa42db1-c659-3493-8487-d7f5c806bd4b | -3.6086 | -60.567402 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4748bc65-27e2-36bd-b2b3-873ab6372b70 | -6.7154 | -59.002998 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b92b7d8-0971-3caf-bcb5-acc6ebae918e | -7.5647 | -57.671501 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb9b6d28-891b-357b-adee-f35a113028d8 | -4.6624 | -56.025101 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe269fac-df6e-3236-bc05-3f83400ac2af | -6.0866 | -57.616501 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 803a951b-9561-3e81-9973-76a7c7a53d4d | -6.0066 | -57.6721 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad250dc-1536-3254-a489-bba02a83beaf | -7.712 | -61.228401 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef1f0695-01ee-3bc3-942f-a198a4af0aad | -6.7881 | -48.694698 | 2026-09-22 01:19:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f079d2cb-1c55-34c2-bab0-97106ea7ee77 | -6.2583 | -55.440498 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df68152-7890-3a20-a5cf-58e8c91d757d | -11.4067 | -46.785099 | 2026-09-22 01:19:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60ad77ff-d78b-3451-a015-1d62e660d54e | -9.6832 | -54.340599 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4fbae10-39cf-3240-b542-14673ffe0ae1 | -3.1867 | -60.4356 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 451dbd8c-083d-340b-b81e-1bd0052a454d | -6.8126 | -59.429001 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa296f9f-c9c3-322e-9055-30197e00f2f3 | -12.8333 | -54.026001 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9b474cb-7a1f-3ccf-a04a-02f2b1e1eb06 | -6.1014 | -57.680302 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7dc57d-ebc3-35e4-8462-831bed332f56 | -6.3105 | -57.736599 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a864eac-fb5c-3a70-9ef4-d467f91d0303 | -8.9197 | -50.896099 | 2026-09-22 01:19:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 452dd006-ec68-3cc6-b8f8-411eb5fb6199 | -7.7218 | -61.226299 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab8a1b8-e7a1-315e-842f-f6be7a775e34 | -3.1065 | -60.715801 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7dffd43-3010-324c-b6cb-4ee3f7c6410b | -6.2909 | -57.7411 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dee8ee-1a46-3ee6-a045-4b34ecdfe465 | -3.469 | -59.553001 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef2efb54-666a-3d6a-9900-825ca45e81a9 | -3.7841 | -60.748901 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec375cd-7130-3c72-8553-c840b9c517b6 | -8.9176 | -50.9286 | 2026-09-22 01:19:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c37bfd4f-95f6-3be7-9df7-41e60dcc2c4a | -12.7984 | -54.052799 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f91546fd-af18-33d3-aec6-3cf79122360a | -6.623 | -59.909698 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12f98cc7-d9ca-3645-b89c-2ccc05eee264 | -3.7181 | -60.550201 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e17aaf0f-ba05-3086-9a1f-03b4d967c28c | -9.8836 | -48.459301 | 2026-09-22 01:19:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee53f13d-5975-3d94-925e-c7461614c44a | -6.0801 | -57.6329 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a943e10-fb61-3173-8b86-17866c2bbc68 | -4.5016 | -59.557999 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44c62d3d-882b-35ba-8765-0f221118f7af | -1.9128 | -58.262001 | 2026-09-22 01:19:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e69871c-279f-3917-a653-87e0715be906 | -6.1079 | -57.708599 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15fdc985-eb02-366c-bb7c-a634969a0df9 | -6.4315 | -55.6059 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8155a90-c223-3b1b-ae84-1f133cc183d0 | -13.9223 | -48.574902 | 2026-09-22 01:19:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e556d057-2681-381c-8481-33c9263c5b80 | -5.4164 | -60.223099 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 437f9745-be16-379e-ae76-d8d9ccc01a4f | -6.0886 | -55.552299 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d087ee-3eed-38e9-ab26-f27dffbea8a3 | -3.3928 | -61.066399 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24818586-11a6-3f70-86c3-eb8d6d483d85 | -10.8769 | -56.241299 | 2026-09-22 01:19:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e62e404-755c-3f5a-aa5d-a49d90ec74b9 | -6.3138 | -57.750702 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a45cccdf-2c48-392a-afba-b0e89d628697 | -3.9359 | -56.050201 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d4efbeb-7c4d-31a7-a7d0-952db302a413 | -7.4029 | -55.2173 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73afe58-bf86-33b7-ab56-7c08ca06dde3 | -5.4132 | -60.209099 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7038a6cd-089d-3115-b59c-32153f3ddae5 | -6.2279 | -55.618 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3f3c4d4-56dd-375e-83c5-3c8d9af8c2b2 | -3.4643 | -59.532501 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfe597ec-ba2b-32dc-a84e-5c59b9abce23 | -18.742599 | -46.937099 | 2026-09-22 01:19:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf062ee6-2fb0-3b53-9ae6-6d6a8479529f | -6.1961 | -57.7775 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 052e1341-9d88-37af-8979-492f7db9d97c | -9.5639 | -66.039902 | 2026-09-22 01:19:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 179d0fda-45df-3c5d-b114-c05c248ac42d | -2.5464 | -58.012901 | 2026-09-22 01:19:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93c29a76-b837-376d-878f-44f75daa0389 | -6.0948 | -57.696701 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f05794bf-f91c-3c7c-97ba-f2b69d3cb9d9 | -8.603 | -54.6189 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d7024a-5cf2-3ddd-9fe6-47bee291b0cc | -6.9189 | -55.615101 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1a0f66-c2fe-3513-af60-f871ff9eab66 | -4.2242 | -48.634998 | 2026-09-22 01:19:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2b7769b-c96d-347e-8ccc-111c85508ecc | -3.0518 | -54.3951 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad5b38b-eccf-35c0-b3c0-b8e3fb667d38 | -3.5073 | -55.4981 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f086b35-b495-3933-9b7b-c1d94338cfdb | -6.1177 | -57.7509 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77afdf13-bdc7-368a-9ac2-b74b3578ced7 | -6.4642 | -59.981998 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95adcecf-6919-33de-b5da-3951ae440cfd | -4.0893 | -62.091599 | 2026-09-22 01:19:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adc5ab15-e607-3e7b-905d-e3a9b3fff39a | -12.7824 | -54.0294 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 111eaaec-d0ef-3434-a554-943dda7009a6 | -6.2926 | -57.748199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9e8f1c-e317-3f33-963a-f7c74bb5e829 | -8.8369 | -50.4855 | 2026-09-22 01:19:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd7d4d5-10d9-3e80-8c87-8637d7ee9f1e | -3.3814 | -61.287399 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a19aecf3-883c-3d6c-b4de-4fa08f8c4bcb | -6.3497 | -57.772099 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94933e78-e84a-353a-ae1f-f0d0addce3d0 | -7.3298 | -55.605999 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b555bd-02d5-30e4-9ff1-ce828337cae6 | -11.4325 | -47.340302 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b227b7c2-34e2-3b6a-99db-03d4fa9cdf17 | -3.4624 | -58.404999 | 2026-09-22 01:19:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67ba2039-68e9-3ba4-b4f2-f71019f18a6b | -6.4202 | -59.9697 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
