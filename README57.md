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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0581ee49-b6fd-3c53-a8a3-29b9a690a205 | -12.95228 | -56.62845 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e263a3d9-e104-3a19-8511-1f84818890b1 | -13.43253 | -43.84969 | 2026-08-23 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 886b628b-cc19-3a60-9dc1-fbd3ca0e250c | -13.19176 | -51.42683 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea6ff589-8f4d-31fa-ac39-d53d6d602f2a | -13.16842 | -51.42343 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 30ad24e4-b4a5-3cf2-93c0-46b9ee2916a4 | -14.50602 | -59.81273 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0882cad4-3beb-357c-b2f8-3e48fa68b15b | -14.31097 | -53.23428 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edb23345-4563-3f0f-902c-2f4c834d121f | -13.39538 | -54.36112 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82566d0a-d4ce-39cf-8e57-62b69cc9a074 | -18.53296 | -47.16022 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c426360-3234-384d-a6f4-a9bf72f937f3 | -18.66055 | -48.18148 | 2026-08-23 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f91012fe-363a-3d3f-bcf8-76366d78ac8a | -14.35102 | -51.77785 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ebbe522-fcaa-3fbb-a4ff-16e55bcf5498 | -14.35489 | -51.77842 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a89a3bbc-c80e-34e1-a611-f13560bb3662 | -13.88635 | -54.00595 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a4b4c3-c3fa-3395-939f-2991526a2a14 | -17.92488 | -44.49526 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21920929-4725-3b21-959b-e62279bed4c8 | -12.73185 | -48.39682 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc0575fd-e58a-351c-9e46-8fa9ac21154d | -13.8938 | -54.00325 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 810e0856-719a-379f-b36c-7f7b9ff7bd82 | -13.16912 | -51.41843 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 11aee5c5-2a45-3f41-aebf-4f6b28b9959b | -17.75338 | -47.03577 | 2026-08-23 05:06:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5baa0ca7-d30e-3c1c-9ef7-09ee00fc5533 | -12.00469 | -53.42288 | 2026-08-23 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 073ec9ec-c7f7-3856-b39c-75985c0eee8a | -13.38464 | -54.36321 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc0abf1b-85ad-3582-a7fb-92531f999258 | -17.63876 | -50.48899 | 2026-08-23 05:06:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b3f4e99-ff75-3a84-97a1-86deb8b1c3b1 | -12.12543 | -57.21344 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6907b8d-d2b5-33e7-b15f-219ee1240a13 | -14.53579 | -52.99722 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5efaf6f5-97bd-36f7-902e-730bc5337551 | -12.74753 | -48.38728 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e820ebb-f1a8-3a43-90af-097716f5a0a7 | -15.24882 | -52.86098 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa37a7c1-57e9-3bad-b508-1aea9adfc267 | -12.75298 | -48.38251 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fdb8eb55-587f-3dc7-a55a-21a4944bb658 | -12.75769 | -48.3833 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfec22bc-fa52-3eae-ac0e-6c94ea1444a9 | -13.7245 | -56.00358 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6c7e3a1-d77a-3660-bbb2-5a25a8be3fdc | -12.74829 | -48.38159 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f59bd39b-86ff-37c1-a262-2d9d57c2f37e | -12.72637 | -48.40197 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13bc6813-fd73-3d73-8129-82963cadb34c | -13.14897 | -51.42058 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 660f436b-1f16-38d3-bd75-adf5a5b3e165 | -14.56116 | -53.00101 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eb449c9-cd7d-3d14-a4fd-fa725dcf4749 | -14.95481 | -52.64958 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9019fda1-79bd-3c10-bc02-7ceaf825958d | -15.76344 | -55.54934 | 2026-08-23 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8783886a-615d-36f4-9721-6516f5508020 | -13.16523 | -51.41787 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5ccd834-2b11-337e-9dab-09a5c7260f2d | -12.85048 | -48.46962 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4bbd2e4-9811-37a9-a8d8-e77eb555473d | -18.51494 | -46.6019 | 2026-08-23 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 395fb49f-15da-32a4-8c0a-2740afc92cff | -11.67558 | -54.5565 | 2026-08-23 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319b7d2c-82c0-31d6-962f-d8a358371bca | -16.05747 | -50.44242 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2ad8251a-a920-3e34-a6b6-e54dfdb7476e | -16.40136 | -51.8469 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbbff77e-a5b7-3be2-9b29-6f4ce48e5212 | -17.62453 | -51.06273 | 2026-08-23 05:06:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70e991a1-c2e5-37e2-ad79-8b1b28f34932 | -14.36225 | -51.83996 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fb9ee13-c775-3f57-ba49-fefa8e3fad10 | -14.3781 | -51.78184 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 838668c2-2e34-3887-a593-aa646817dd7c | -13.44407 | -57.07899 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac1e86e2-e630-3c10-9058-addc2cfdb944 | -13.1808 | -51.42014 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee674832-38f4-3d93-9582-69282a30625d | -14.57257 | -53.02449 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ab4d467-9557-36c0-9ef0-3f14f937f671 | -13.39143 | -54.3643 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 035c76bc-d2e7-32fd-bec7-a67f046cab98 | -12.94953 | -56.62433 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d41a16-6e08-3b28-a6ab-dcf7f28aa937 | -17.93092 | -44.50072 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ac9857f-0abd-32f9-9fe1-adde58e73157 | -13.43739 | -57.07787 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfee2474-fb08-3b95-9329-209918062e83 | -13.59415 | -55.1652 | 2026-08-23 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f5b90da-79bb-3d38-b3c1-6f002ec99af7 | -14.95417 | -52.65405 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1c24aca-b9f6-38a4-83a7-38d5b19b7d50 | -15.24585 | -52.82911 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c40eb6f-f7a5-3367-b487-b0723b41c280 | -12.74199 | -48.39278 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0ec903b-d719-35ef-ba48-328fa77c77cd | -13.83928 | -54.01435 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bdec5c5-a41e-3d34-a2cf-a96c8c8864a6 | -12.75929 | -48.3798 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fbb520a-dfa5-35cf-a266-961ff87699be | -14.57619 | -53.02504 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 963724b0-673f-3efe-b3a5-cfd877511026 | -13.16453 | -51.42286 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c95b23ef-55b7-38e3-b851-2019d6a13b0a | -14.56771 | -53.03252 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de0b9080-0a94-34e5-9e62-665556894a74 | -16.05039 | -50.42892 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f234c02-fb62-3a9f-9a37-7288f814c20e | -14.58527 | -53.0134 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 703daab4-283f-3f28-b715-d5643f2488c4 | -12.95561 | -56.62901 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3b761f2-b728-3322-84b4-751a80d0cb9c | -13.99477 | -53.71848 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f6e716-9a49-3c5d-9c99-b0f959f37b25 | -18.66206 | -48.1793 | 2026-08-23 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d390869f-9635-3e68-9fe8-c469fcf18345 | -13.15535 | -51.43169 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6c30f419-684e-33ac-8d24-3cd47256d2f9 | -12.7542 | -48.40947 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 157b9e08-4bfb-35cf-a7d2-1ffdd6cd0313 | -14.96705 | -52.66978 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dd8a7c3-968e-355f-ab2b-372ffce3d6ed | -14.3661 | -51.84054 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4603b71-9a4b-3e8c-a22f-6cd5f9477f28 | -12.09473 | -58.19924 | 2026-08-23 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec1e466-00b3-38ce-a37e-598eda27ec02 | -12.85112 | -48.46455 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| be7b1f23-ac42-36b3-8447-e3ee4d4a2f4e | -13.15924 | -51.43226 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ca297e84-2f4f-3db7-a578-7fa07d19a250 | -14.35766 | -51.7764 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55568809-a22f-3c57-826d-dd149d7fcec0 | -12.94345 | -56.61964 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183249c1-15e3-3a8d-a1a9-17c314591d52 | -15.7598 | -49.96888 | 2026-08-23 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ec8de43-8081-39ca-b888-4bbffd9e798f | -14.33832 | -51.77357 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 317e45e3-0716-3f5a-9161-53a60d6c45f3 | -14.35379 | -51.77584 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df50e57b-99ba-3cb1-b611-9676556ae691 | -12.58939 | -47.88511 | 2026-08-23 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61c0d16b-b221-3674-bf14-871b436e715e | -13.58747 | -55.16416 | 2026-08-23 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 219d0d7f-c7be-3020-9d5c-815d5a473a28 | -15.3152 | -53.79625 | 2026-08-23 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b638ec9-e367-3955-a5a3-6c44f5f9e146 | -14.39358 | -51.78411 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94a5eb2-1916-396e-ab16-1fd649cd174b | -15.75922 | -49.97337 | 2026-08-23 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b8e876-70d3-3115-a403-b37013cddc3c | -14.15123 | -48.06802 | 2026-08-23 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a48ca296-1d1b-3e93-9f1e-92e841c23678 | -13.88978 | -54.00654 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a37e536-7777-3a96-8848-01cc55b77c23 | -12.74413 | -48.413 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7670c5f4-9138-3ae5-83f7-ce0f6ce84644 | -13.4313 | -43.86029 | 2026-08-23 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e436a84-dc8e-3226-9c75-5d910e2888df | -16.06284 | -50.43466 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d018000-f1c4-34ec-bedb-0505da6cdcd5 | -11.68954 | -54.5771 | 2026-08-23 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fba31dbf-b5eb-307b-a3e0-cd21fd804d8f | -15.55354 | -56.31232 | 2026-08-23 05:06:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15e173f4-76af-3b47-b7ce-4691e76c424f | -14.50039 | -59.82762 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66d4b94e-b410-361d-acd1-201f1ae0d448 | -16.40278 | -51.83609 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 930ea496-6d51-354a-992c-937940f0b0b1 | -12.83778 | -48.47857 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5763e60-fa14-3c3d-a8e9-97c5d9793e69 | -14.56347 | -53.03625 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c09384d6-f4dc-3643-9978-51b252a855be | -14.50118 | -59.82302 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d062064-0fd6-35bc-9dfc-b28ebc667c68 | -13.16064 | -51.42228 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 064b1153-f949-3ad5-8e4c-ea8dab5e281d | -14.43791 | -51.80576 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8168904b-2f0a-358c-a5b2-ea9168802e2f | -14.57681 | -53.02077 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4d018e2-59ed-3f91-9be8-b500396476ac | -16.04987 | -50.43307 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1f87a2e5-f37f-3043-a610-f26961490db2 | -13.46042 | -57.05555 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cd84234-b955-35cd-94af-0f00ca1c10c2 | -15.51774 | -49.82996 | 2026-08-23 05:06:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add68575-8002-31e3-9947-b91b3eefcd3c | -12.75536 | -48.41109 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f94e1c39-8026-3cc8-b162-1d1ca61b2eee | -14.43118 | -52.9212 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
