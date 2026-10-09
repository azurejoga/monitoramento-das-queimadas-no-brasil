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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04e1cf97-dda0-3d64-89ba-79fa780f2264 | -13.1654 | -54.31829 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cab4b18-a219-3036-b448-582ba0858bdb | -15.94852 | -41.07958 | 2026-10-09 05:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ac6f86fb-4975-31d3-af06-25f0a7266fda | -15.11865 | -48.52646 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f96ba9dc-802c-3dc1-ae5b-b920e97765d3 | -11.76917 | -58.2838 | 2026-10-09 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a7c995a-1549-314d-ab3a-fd4f787be084 | -12.22306 | -57.10927 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| efa82716-efbb-3142-ba96-b812b10f182a | -13.19799 | -54.37111 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| da905a61-29da-3f76-bd3d-7ff370dcebff | -15.25867 | -42.3672 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7745bbbf-bb65-3eda-93b3-714d5fcf37ce | -14.97578 | -47.54426 | 2026-10-09 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14a7f741-50a5-377e-ac1d-9dc641bb8892 | -14.52044 | -49.33169 | 2026-10-09 05:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 962a55d9-f3ed-3a0e-8207-b4ac97c08d0c | -13.1542 | -54.34558 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b17c851-28aa-38ee-a41c-99958628ccf8 | -13.18319 | -54.31396 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 978886de-4892-37fe-83d3-be3b1d9c1eac | -13.19742 | -54.37466 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 71af04f6-ba68-3113-9b75-4c47af4ebf7a | -13.16037 | -54.32839 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6490466-9226-38a6-a031-6f51e34da83e | -15.78182 | -44.6842 | 2026-10-09 05:06:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc3d3ba5-e518-3430-ac1a-cd714fbd2ccc | -11.75355 | -61.06574 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7f127cd9-e1ff-377e-bbd9-3153af3986f8 | -14.05241 | -43.82742 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af8db1a-ffbb-3735-8b28-48d018ce0bd7 | -15.21875 | -47.89517 | 2026-10-09 05:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f138ce2c-9d49-3aba-ad51-a8f4208adba0 | -15.89052 | -46.46896 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76b9f3b8-0c23-3fb0-ac0c-6857792d97e5 | -13.20855 | -54.36921 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34292b72-86ad-3770-8c31-5660e3efb0ae | -9.25777 | -62.30891 | 2026-10-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93c8e4aa-e32d-32b7-9d94-9cc5c389de8c | -13.20969 | -54.3621 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17378d03-169a-3f98-b6f0-167cef07d1f2 | -15.7342 | -50.80081 | 2026-10-09 05:06:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baac4afb-7e1d-3fbc-bf1e-61e8fb9bcdc2 | -15.42966 | -43.243 | 2026-10-09 05:06:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4c8558e2-c106-3744-8185-31b510b6fd53 | -13.349 | -43.96669 | 2026-10-09 05:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb0ccc62-3db6-3b24-9588-51345fd5eb18 | -10.67434 | -58.73512 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f36b00e2-802f-366c-be24-4abfd056aabb | -15.95548 | -41.08053 | 2026-10-09 05:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9d56b785-c070-36e3-8aed-825190138fcb | -11.78894 | -46.79423 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| db7757e9-37ee-3818-a73a-fcb89786075a | -16.12501 | -43.74139 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57bf0161-c4e2-3efa-aadf-01a70bc13cd7 | -12.2158 | -57.13001 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac2ce240-da2c-3a49-b229-59c243b274d7 | -12.24265 | -57.10399 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84d32c08-552d-3347-9582-0de0a3b6b28d | -10.85594 | -59.11384 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff64fc3d-337c-31cd-acee-e31c67137477 | -13.16753 | -54.3478 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 369a872c-4ef9-349c-9e50-b017c0a1fa19 | -13.25087 | -42.24854 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 937590ac-ae97-3a6a-8cf8-c117cd45d853 | -13.18913 | -54.36233 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 060b4886-ae67-3fc8-9342-a66fb3b9e0fb | -15.25287 | -42.36054 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d2544971-f9e0-39e3-887e-a2ab3e9e58e9 | -15.10029 | -43.63827 | 2026-10-09 05:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5cdc2f82-5bfc-3eab-9a64-ac101cc7697b | -14.05257 | -43.82934 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 765ffa3b-37a5-351b-9ed1-0dcf72baa817 | -18.08185 | -42.27049 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6d0a3da3-25cc-32d5-993c-76eda65d65ac | -15.94852 | -41.07957 | 2026-10-09 05:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9a2fb9f4-1e39-385a-b757-305b7be13a7b | -10.85082 | -54.02601 | 2026-10-09 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7b8025-5789-3c10-a38f-1b606e0220be | -13.41234 | -43.72797 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e93e488-e328-3c69-9932-edeb5c38bf82 | -12.23029 | -57.08858 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2a4016bb-d11a-3fa0-9801-c3f8d90b4e9f | -12.20417 | -57.1323 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbe18b52-8042-3bdc-9012-2fc04267543b | -13.26246 | -44.00179 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dbd8f99-8c2f-3f4b-b6c9-686ce37a6f7c | -18.08549 | -42.26435 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 57debecd-9fdd-31dc-b2bb-c815630a3b37 | -12.1969 | -57.131 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68f11916-61fe-3e19-98b1-24f14522a1e5 | -16.96058 | -46.35522 | 2026-10-09 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ca19c0-cb9f-3c2c-8ea4-74dec564ceef | -15.21818 | -47.89962 | 2026-10-09 05:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 136b7241-73a0-32af-bef2-83eef12a5ce0 | -13.1732 | -54.31229 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3cad872-a593-3a9f-94d7-b8fb15e7419d | -13.36452 | -43.88455 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae4a45bf-4410-3627-85c7-0357def26fd2 | -13.18247 | -54.36122 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bc11a91-8e8f-39bb-a642-7c6d04f2d557 | -15.08456 | -43.11469 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d7e65353-d462-3690-bbb3-275009a266d8 | -12.19146 | -48.41567 | 2026-10-09 05:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa685244-d29e-3655-b3a8-9831cc1a8d73 | -18.32455 | -42.37809 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| dfd31e3a-272c-3e85-b804-40f07cc93c4f | -13.25722 | -42.2491 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2811acee-406e-3697-9d2e-b2cb25da1b98 | -13.15201 | -54.33792 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9944ebbe-87cc-3be1-8a09-b06654505f11 | -15.5158 | -50.41088 | 2026-10-09 05:06:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ffb2f23-4557-37df-86b0-0c5bcd3daa25 | -11.79226 | -46.80457 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a8e34261-eeb4-3ac2-a6aa-80a9b27a75c4 | -14.87824 | -50.30088 | 2026-10-09 05:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0b891bc-c8a4-34e5-bb51-f1a92bc4d2b9 | -16.57235 | -51.62671 | 2026-10-09 05:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06c5903a-0a65-3f6c-8af2-36556f0637d5 | -18.32899 | -42.36573 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ec00e4f4-14b5-36b7-a83d-216427d54cd3 | -16.12422 | -43.74875 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed49932c-dea0-3de5-ad0a-984229859521 | -13.25044 | -42.25234 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a97ea4fe-c42b-3583-a087-f7c7833c2bc3 | -12.19763 | -57.12674 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a695520b-1d05-3ea2-82a8-f168e7a44416 | -12.78172 | -60.60673 | 2026-10-09 05:06:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87a21db-78cc-3b1f-b4ea-58f31f2c2859 | -13.63484 | -44.42539 | 2026-10-09 05:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 580cd916-bca0-39ed-b47e-79508b8d094a | -10.67722 | -58.73477 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 901ffae9-4522-3bc7-8287-eb7f393187ff | -18.62877 | -41.34631 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aafbf995-4487-39c5-a172-546cce7e54cd | -21.9696 | -55.93521 | 2026-10-09 05:08:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 457e3638-8fb3-3a70-b0ac-8580cc537562 | -21.97293 | -55.93581 | 2026-10-09 05:08:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce569cc8-d81b-3134-ae29-91a6391a4eb6 | -17.84389 | -52.3895 | 2026-10-09 05:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91039095-0215-321f-8fb3-a9953842b9c8 | -21.97352 | -55.93208 | 2026-10-09 05:08:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25b1271b-129d-3b0b-8620-84ea074b4765 | -18.64288 | -41.34804 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c273bc8c-0c2f-3f96-85e3-0f1b8abf993a | -17.41161 | -52.01829 | 2026-10-09 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d5c3fad4-0016-3ae8-85a3-ac7ad4825096 | -18.78702 | -46.47046 | 2026-10-09 05:08:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2856cfb-3eb8-319d-87dd-ca1c2d02df7b | -21.70133 | -56.00265 | 2026-10-09 05:08:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73afc6ec-92e7-3b05-b99b-94892fb9d11a | -19.99148 | -49.08644 | 2026-10-09 05:08:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56788ee6-60fd-3877-b3c0-eb10bc6ee515 | -18.63522 | -41.35444 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 529a9293-6ecc-32e0-a4fc-8492d574d5f0 | -18.18702 | -51.78138 | 2026-10-09 05:08:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f604464d-1fe7-3599-aca4-f0bf8e9b9150 | -18.11345 | -54.51936 | 2026-10-09 05:08:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc3037a6-edd5-3c96-8aba-e663743df65a | -17.83214 | -52.34502 | 2026-10-09 05:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 332a0acf-4059-31a3-83b4-e3b6635dd9b7 | -19.33058 | -48.73233 | 2026-10-09 05:08:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f75d8b9-b68e-3405-b02f-b631c2895529 | -18.63153 | -41.35521 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 01ae66e4-864b-3747-b603-0af7b8eac4aa | -18.78739 | -46.4671 | 2026-10-09 05:08:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 723e4d8e-6906-3da3-94f3-00ecdb34d619 | -17.8292 | -52.34016 | 2026-10-09 05:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3521fca9-97c6-3686-a312-9dd451e8e0aa | -18.78187 | -46.46956 | 2026-10-09 05:08:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86f74f64-e25f-39c6-95d0-b486883ee658 | -17.82858 | -52.34448 | 2026-10-09 05:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8926d192-2f64-3de4-a69f-01e203b70c78 | -18.63643 | -41.33994 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8aa68eed-8152-3adc-819d-222ec2c1932b | -17.83276 | -52.34072 | 2026-10-09 05:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfa3537c-5285-3dd5-8970-ec69d2186723 | -19.99589 | -49.08712 | 2026-10-09 05:08:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a69eb866-08c9-36fb-841b-caacc579bfe6 | -19.32882 | -48.73503 | 2026-10-09 05:08:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec463511-99b1-327d-b156-3bbdbdda4ac1 | -18.63212 | -41.34861 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1d15c1b7-d7a9-359d-b943-80a7fa5c8f19 | -17.411 | -52.02257 | 2026-10-09 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4c61f0c-6bd1-327a-8331-9f4afc9a849b | -18.62824 | -41.35266 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c4d771c7-4a94-3f70-b0d9-d59bee30d6c1 | -18.63212 | -41.3486 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d4bfbeb2-aa3a-3361-b913-47d118499433 | -18.64288 | -41.34803 | 2026-10-09 05:08:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 29e6c0e4-fae7-34eb-acb8-f4b1d123eac8 | 4.01571 | -60.34372 | 2026-10-09 05:21:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18952c4f-7fbc-3a05-9c9d-8afe3fb96016 | 3.52869 | -51.24813 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf562bb1-9797-3b3e-9a06-8b7038b26c88 | 4.01504 | -60.33942 | 2026-10-09 05:21:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b43ba210-aed8-3106-a293-8de0a83923c6 | 3.73259 | -51.65057 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README177.md)
