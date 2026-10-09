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
| 06f26699-e219-3229-9560-c4d56bfc7d56 | -5.40469 | -45.64616 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a48e32-9a20-33a2-8d75-11ea43de2e37 | -4.63517 | -50.9542 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03881198-3a25-3ba5-9a5d-d162ea8049f9 | -2.74291 | -54.10649 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e65b8ef-b2c0-3dfa-9dd7-9a5fa071cd8c | -6.15597 | -47.2823 | 2026-10-09 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcaf63ee-c1a0-3470-a498-9ef6b31c2b17 | -3.0164 | -51.01234 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 172cf2cc-7a35-3084-bf7d-7fa587e34ad5 | -4.26703 | -46.28437 | 2026-10-09 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48416fa5-0c63-32f9-956b-8831d39300ec | -3.16221 | -57.68233 | 2026-10-09 04:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c800212-bbb3-3334-9724-5d93abded01a | -5.062 | -46.18845 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60f96fe7-faba-3c6c-93da-d078aa951eae | -2.99645 | -53.90914 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34fb896c-c6cf-33fd-9378-ae49fba755af | -2.4685 | -56.06326 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08ee42ea-2b0f-3249-8bbf-5355272c0d1c | -3.2796 | -54.06373 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccd401c1-7033-33a5-836b-f1f055f53140 | -3.55209 | -54.69487 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00b2c249-1334-3a6c-a896-9f1971ced03e | -4.62056 | -49.20712 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7abd2b0-9dec-3c37-b5cb-34c23c952386 | -7.38375 | -39.97298 | 2026-10-09 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87e5d266-c2a3-3d7a-adb2-cab5230df428 | -3.31303 | -54.70662 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bc6ba1a-9080-30d4-a611-614d42d167b3 | -1.62901 | -55.12884 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7290ef1-fdbd-3214-b11a-5bfc1773f421 | -1.79624 | -47.84763 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4352e04-5d7e-3feb-b4e0-c87fffc6ccd2 | -3.01889 | -54.08885 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a51c1cd-027d-3487-aba2-94da1308dedb | -2.89861 | -57.20914 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a84175d-6401-3b3b-bc87-ecc038c5f63e | -3.0098 | -54.10553 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e5b781-c825-3d40-9c7d-828f52a7882b | -3.55885 | -54.68626 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e81dda2-4d9a-3314-87a2-c3d117d6e28a | -3.17338 | -54.7355 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bf87fcf-2872-3c12-9ed9-4b3d48b2460e | -2.99359 | -54.08489 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b0f66fb-9d45-33ee-b5dc-09a1c1be8987 | -3.86766 | -55.99413 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbd5dd63-d940-3384-bc54-c945e3924783 | -3.80718 | -49.93984 | 2026-10-09 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 444e68d9-ab8a-311a-b384-94d96a7b45bf | -3.81864 | -44.59719 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23c8c8e5-ba4d-364c-8a18-76639c796919 | -3.10429 | -53.94093 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f600aeda-51d9-3a35-a557-1956a645a489 | -3.1097 | -53.93924 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11a6cc93-8cfc-303d-b600-26e0d071748a | -3.54528 | -54.67098 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1ecf724-55dc-39f7-9bcc-77ddb5e83793 | -2.76079 | -49.53367 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0043e7f0-66b3-3c31-9fef-7e81919097ac | -2.97939 | -54.07655 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae9487f1-37a9-3935-8b4c-ef8bbd581789 | -4.74356 | -55.65583 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6096bd0e-7c23-3451-9941-200e5c1c4d20 | -2.88341 | -54.1837 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41e633f5-f379-32ff-a074-243b643644b2 | -2.76275 | -54.11283 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 936c6d04-a876-394a-8f18-da7781cd740f | -6.01154 | -42.26057 | 2026-10-09 04:25:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6f305d4f-f854-3b6e-95ca-c876d348e014 | -3.304 | -53.70393 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cdd6c7f9-0194-3b53-8025-c48d792e10c3 | -1.11458 | -54.17112 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aa9955e0-6bbb-3c8c-835f-31c7d9e6133d | -6.50207 | -43.95201 | 2026-10-09 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f05c057-fc5f-3a16-a9e7-fee217d73768 | -3.17023 | -50.45786 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bbf0b1c-37ad-3cef-be17-248bfbb2f557 | -5.40416 | -45.64963 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60299098-3922-3071-ac5f-e60349b1485d | -3.21727 | -42.9645 | 2026-10-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18769ee3-5d5e-3688-8cea-20697e84312f | -3.52213 | -50.34528 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3450e86e-ef8f-3eda-9cc9-c152ed8d8a5a | -4.10815 | -54.62511 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94254cac-fc2e-317e-82d0-214de5956f19 | -3.27604 | -54.05415 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec01710d-bb31-3d18-ad1a-c7e508e84d85 | -5.71909 | -53.498 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bcf2251a-467b-38f2-9284-7d0a031ba246 | -5.70813 | -53.47042 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6307c799-5504-36b5-91bb-9a57b3a132a3 | -2.87936 | -54.1881 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10eb42fe-64cc-32ce-8a7e-cab8f40f818d | -6.19704 | -45.40492 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77218e07-eab6-32a5-861d-19f6a1efc73d | -5.98133 | -41.37904 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| def4709e-2004-3707-a421-4d3c0bcdbac7 | -2.78476 | -54.07339 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6765bc11-f869-3b60-8341-3227af6ad98a | -3.90267 | -55.89291 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5759ca99-365e-308c-b83a-05449c37186b | -3.58669 | -54.68388 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b94da76b-36f1-36aa-bfc9-a7c0edaa8c94 | -3.03969 | -54.27095 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fd7d5d8-ced0-3da6-885e-75900ed53913 | -5.09283 | -46.20731 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b95264-f926-3013-9d20-9b9f123f9955 | -3.04173 | -54.25855 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1466351-063e-3e38-ba24-86ca3e17d34e | -4.08856 | -44.12172 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 505e47d4-b392-3507-a940-5df13f40252e | -6.85576 | -41.75601 | 2026-10-09 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 39539271-d685-347c-ae37-16634fc47686 | -3.20279 | -50.55648 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1bbe906b-7a40-3c76-bde3-8bd00ddc6fc2 | -5.98535 | -41.37962 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7a0ef26-0356-3891-9e4e-52a648d0b702 | -1.42858 | -54.62368 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4759ab60-4d61-34fa-af1d-83abe955dc95 | -6.88617 | -43.70614 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c5db72c-c4db-310a-8555-ee272bab8318 | -3.60692 | -54.56413 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef8245f2-c1f5-3e74-944f-ac413775a6a8 | -2.7434 | -54.10349 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ce3fd88-4684-39a4-b023-94c0aeac4e3f | -6.15142 | -47.95814 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ef4bd5a-a8d7-3feb-84d7-299afc2faac9 | -1.53886 | -54.5531 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 448bf61c-b1d4-320b-bd87-1153df3d6303 | -6.00875 | -40.96872 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 2c9e8672-7e08-31cb-a385-0a1606d2b719 | -3.5526 | -54.69176 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a6326a1-d1dd-37e8-a1ab-8dfca2dd0686 | -1.26458 | -54.68279 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7a2400-ee6d-3001-863f-d3023d817209 | -6.15479 | -47.95866 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1d53507-5408-37aa-9341-080b2e0331eb | -4.80614 | -42.74197 | 2026-10-09 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4875966a-a7b8-3897-ad83-4134b554be66 | -6.00515 | -40.96447 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9b901314-0d44-3df2-aac0-e6e3b6de618a | -6.68608 | -41.76083 | 2026-10-09 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42d8a3eb-9202-3d93-89e7-1bd8e85cdc2a | -3.98479 | -59.35817 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0f09c7b-55bf-30bd-a3b7-3ae6b2a75c2f | -3.20387 | -50.83162 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0492fdbf-1d7c-3401-877e-355d307bc70f | -2.39013 | -57.89726 | 2026-10-09 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99f15644-bd80-3774-b62b-1893500bcc26 | -4.29899 | -54.80947 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e898128b-89c5-369f-86aa-1a6e31fb3b09 | -3.09642 | -53.95765 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fdc4fd6-2bf8-3f61-9ec2-2d50d1f6bbe7 | -3.01536 | -54.10335 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baf211e8-87d4-32c9-9b19-c3c41109410e | -5.59767 | -47.28366 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0da1a357-d290-3c50-bdbb-7338f154d1fb | -3.02379 | -54.05332 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab002dc-2113-36a4-9fa8-e48e53bc228f | -4.74288 | -55.65981 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1df760d-6fe8-33a1-b3dc-0c0e82d21136 | -1.38557 | -55.19926 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9903a71a-9c63-3360-9228-a78f2fb12297 | -3.25429 | -54.03012 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1953afb0-1923-3b5a-bd23-212d85ee8952 | -5.75997 | -43.85252 | 2026-10-09 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22e9d514-c2ac-38e9-a6fb-9d74da9d9770 | -4.10583 | -54.02073 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0059639-89c9-34aa-8193-d3f4ea4164af | -3.27359 | -54.06885 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d976b173-3ddf-3370-ae1e-91dfbb1db830 | -3.02595 | -54.0448 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15e15dc-a3b4-3bc6-989c-526b50564570 | -5.99832 | -40.98245 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d018410b-5fed-322a-8718-122b3650335d | -1.10936 | -54.17016 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65949676-ec16-3872-b1f7-edbf3abafe57 | -4.54272 | -47.04527 | 2026-10-09 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec04d01-0319-39aa-8938-ac029367febe | -3.56945 | -54.69069 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bec9ef02-00a4-3e8b-bfa4-76bf1dc931e8 | -3.11349 | -54.194 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19bc7ae1-a098-3234-b25d-becf80eda316 | -5.27839 | -45.71463 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5816faa3-28d8-3f63-ab6e-6fa179bcca3b | -3.85616 | -51.93475 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6436df0f-bdaf-36da-b150-803ad6094620 | -2.77825 | -54.08149 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd5a66a-1789-3078-9eab-389a3887ea98 | -3.29824 | -54.01335 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4d94dc5-764b-3f9d-8db3-29bdf789890b | -3.00041 | -54.76781 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c74835-1799-3f5a-b024-3c30a0ff4e07 | -3.06027 | -53.92795 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e134cc3d-d9dc-3d2d-a943-0af57e1e5330 | -4.26649 | -46.28782 | 2026-10-09 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea6c1572-6f33-3ca1-87ad-444534a12496 | -3.54737 | -54.69093 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README82.md)
