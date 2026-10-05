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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be94c677-f55e-3f74-ac1d-53869b4a0c4c | -10.33659 | -39.49368 | 2026-10-05 17:13:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 8145d5f7-211f-34bd-aba0-f083b643aeed | -11.34045 | -51.31084 | 2026-10-05 17:13:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e07fd89e-4bfb-3281-bb30-957a0a26ef42 | -15.57004 | -40.9272 | 2026-10-05 17:13:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 49663b79-bdf3-33d6-a549-e2492cb65a50 | -11.80178 | -41.59916 | 2026-10-05 17:13:00 | NPP-375 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 406da08d-32c7-32d5-9e05-7671320f709b | -10.36872 | -45.02299 | 2026-10-05 17:13:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 96a0c6f0-c08b-33b1-b926-1188f163d63f | -11.63437 | -43.63352 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dbde63fb-bd64-3cf9-a4b9-6be692e524cc | -10.4924 | -47.23917 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 4001801f-15c7-3ac9-be38-fbfdc0ba4ba6 | -11.37072 | -47.52223 | 2026-10-05 17:13:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d9af71c9-16f6-3bc8-8ee0-5a4583ea1f22 | -13.93485 | -40.21914 | 2026-10-05 17:13:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 63328030-2581-3412-ad01-cf9c1a380874 | -11.83346 | -43.54477 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9481f3b0-6de8-375a-9c4a-22aa70004920 | -12.81641 | -43.3149 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ce0b2fea-c7fd-32db-9e8a-0b0d9d70a3c3 | -11.36602 | -47.70997 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38a450b4-6c42-3f1d-8216-56aa94ccadd4 | -12.76733 | -44.19874 | 2026-10-05 17:13:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6d0af828-e6a3-38b8-93c4-7153f8d2d516 | -11.45388 | -47.73373 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6082ee45-fd2a-31bc-8a95-405570e10c39 | -12.55784 | -46.67818 | 2026-10-05 17:13:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7c363f2c-1a27-392e-9bf1-7b7223ed00c4 | -11.68703 | -43.65937 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eaaa0a7d-ce0f-3014-8ac0-717b0c5be9fe | -10.97139 | -45.42177 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9eb0fb89-22ad-3f42-9800-d92bacddb0c8 | -16.32967 | -41.9474 | 2026-10-05 17:13:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 58c79d2f-b050-31eb-a161-d3e38b97420f | -12.81347 | -43.30502 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 0e6fdd66-efb8-37fc-a52f-d00de589fd64 | -11.63538 | -43.61044 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7ca8a458-a860-34f5-813b-2ad1bda7a501 | -12.58088 | -47.22203 | 2026-10-05 17:13:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aeed4574-028e-329e-b6e1-c0bd88a1e2ce | -14.07876 | -43.76746 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1740a473-8f81-371c-a3d7-1d4b59965c7b | -11.64749 | -43.61814 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b6ef0aea-b07c-3d3d-bd0a-94b68303cfc5 | -12.7608 | -62.05505 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fcca1210-08e7-3732-be53-fa568875c53f | -9.85778 | -44.81524 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9d478d9b-4b26-3d04-ad09-eb9dfa833710 | -12.04581 | -43.44087 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d22cd36e-72be-36de-8dcf-1e9764ca387e | -11.19019 | -50.80193 | 2026-10-05 17:13:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 024a7d3e-b710-3e5a-b09f-1ad798e33320 | -9.01974 | -39.9522 | 2026-10-05 17:13:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 01319532-d607-3243-9145-a860b3c09c7e | -14.05071 | -42.49379 | 2026-10-05 17:13:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d253878-4c8e-3d4f-ba59-5545abc27adb | -10.49164 | -47.24415 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 41090049-0dd6-3095-b885-5caffcf35f02 | -13.60304 | -42.49607 | 2026-10-05 17:13:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| fc342a5e-e949-3cab-9168-92c4a6b9cdbd | -14.63087 | -40.57142 | 2026-10-05 17:13:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8b93c94e-4f9b-31e6-9224-32781b1488e9 | -11.19017 | -50.80166 | 2026-10-05 17:13:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8fc78443-54f1-35b6-af08-a3566ce08aa4 | -14.62995 | -40.56708 | 2026-10-05 17:13:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 926e513d-54a2-339f-8b14-68162bafbd3f | -11.81054 | -47.36657 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27c5f665-2b97-3643-816e-bc5f8eeb70b3 | -10.96309 | -45.42865 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4365fd67-847b-3619-98ce-808d9890f019 | -10.36393 | -45.02392 | 2026-10-05 17:13:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| a4039f5e-23fa-3e38-ac3d-659ebfa337fd | -12.8757 | -62.15107 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd7e22e8-41b3-37da-bcb7-a71e06cc3380 | -9.86132 | -44.80048 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fa4b22fe-b297-3d42-83dd-4fa461143078 | -12.92402 | -62.17266 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9ff9bdde-2bcd-3015-95c4-41dd7a449d1b | -11.62921 | -43.63446 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f1ebca0f-6c81-3957-8c85-b6c3086a204a | -12.05095 | -43.43971 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86ce3c6f-032a-34fe-9139-919190010ea5 | -13.51641 | -61.12808 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aac27c82-2041-3217-93ed-ec5af8e1fdeb | -11.82234 | -43.54247 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d880df34-e3e3-39be-a3cc-ebd1d2f290b4 | -11.82195 | -47.36095 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f09a9580-a2a9-383e-b7ab-38a0f70f70e3 | -12.01889 | -62.52348 | 2026-10-05 17:13:00 | NPP-375 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77f1f8dd-8c22-3d90-a70a-5c23ecbee290 | -13.5046 | -61.11932 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7a8af04f-a8dd-3986-8116-380744bc4078 | -10.48829 | -47.24001 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 5a2d489d-7320-391e-8163-7deb56422e5d | -14.00142 | -41.49794 | 2026-10-05 17:13:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b119caa-b1c5-32e5-9a8a-ef7bac30ff82 | -11.823 | -43.54599 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a478171-2934-3f6a-be28-b4f48030bfdd | -15.33762 | -42.77506 | 2026-10-05 17:13:00 | NPP-375 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c710d129-3d6b-3254-8bb7-4476cd1b491e | -11.34667 | -46.65317 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f7404437-f035-379f-9c7e-f498a142ebd8 | -13.50724 | -40.84006 | 2026-10-05 17:13:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 520e2f73-7a95-3ec9-8f5f-045cbaced971 | -11.07015 | -47.49464 | 2026-10-05 17:13:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdea3334-1a48-39c0-90cf-d126b5b3fa3b | -13.52508 | -61.11007 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| e63f656c-6956-3db7-90ee-ecb806778990 | -11.46035 | -43.39482 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ecd3fcec-650d-32e2-86fe-f114b8580897 | -12.50908 | -41.21071 | 2026-10-05 17:13:00 | NPP-375 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2903059e-494b-38f7-b98a-19c8043019e2 | -12.81519 | -43.30864 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 5d8f6897-f857-37e8-abe0-9bd731d3c1ae | -10.9503 | -45.43696 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 99b97f3a-16cd-3937-a95b-51e65acff803 | -12.77008 | -44.20076 | 2026-10-05 17:13:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 56053993-44a0-35db-9e8b-d852316ccaba | -12.8095 | -43.31231 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5438d2ed-7c36-3627-a7ed-d400e6ff3a3b | -12.5716 | -47.34544 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c42b8f1-eff0-3778-9847-764dec07c412 | -15.27017 | -42.18791 | 2026-10-05 17:13:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 055762b9-d77a-37c3-967b-d2222d66c437 | -12.55925 | -46.67831 | 2026-10-05 17:13:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e558b1e7-b0e0-345c-81f2-b51f507b2f57 | -11.68648 | -43.65637 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 98cc1829-3aa2-33f3-ad7e-4dc4f232890f | -12.90163 | -40.07717 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 29c17dd0-5979-3815-adcf-33f56be14b7d | -12.16102 | -60.74882 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7e39db25-02d5-3298-9639-608278e5fef6 | -11.27609 | -47.67539 | 2026-10-05 17:13:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c3f20b3-ffb2-32b6-87eb-7871c7174ae9 | -11.6509 | -43.6078 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15547300-1f0d-3caf-9089-16bb7db369ca | -11.45511 | -43.39579 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6b9f0a09-df9b-3329-9a77-5aa7faacaef4 | -11.45973 | -43.39153 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f83bf44a-9d3a-328d-82f0-a46e463c3340 | -11.44986 | -43.39675 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5a559507-a124-3af4-b531-22243c250001 | -11.71374 | -43.42276 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4e7ec2aa-19c7-3745-8645-b3268b5c2478 | -11.63041 | -43.64082 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 344fb84b-3d1e-34ed-8bc4-46d88795598d | -13.93398 | -40.21499 | 2026-10-05 17:13:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| ab675910-883f-3500-af50-1e62d702f843 | -11.3805 | -47.72319 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9ce24db0-4e68-3afc-ba28-5b324d940a31 | -10.98119 | -45.44971 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7b79e475-c609-3219-bc6e-cad04cee0540 | -11.18678 | -50.80249 | 2026-10-05 17:13:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d78d43db-9615-3a4a-9d95-0fd2e378693d | -16.1527 | -43.87749 | 2026-10-05 17:13:00 | NPP-375 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e140876d-13d2-30de-8db1-382aff42975f | -9.86238 | -44.80628 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 24c3c52e-d3ef-32ba-b75c-a73ccf5d641a | -15.3372 | -42.77293 | 2026-10-05 17:13:00 | NPP-375 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e398218-364a-33d9-b40c-12992c10418e | -14.85468 | -41.67265 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f1a09870-c63d-3bce-8536-93deceda5bb3 | -11.68222 | -43.65215 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1518fe25-dbc3-3502-8306-4452c6cf4542 | -14.31963 | -42.40861 | 2026-10-05 17:13:00 | NPP-375 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| c9183fc5-f4ed-38cb-93bf-08d9bbc76029 | -14.69233 | -41.90821 | 2026-10-05 17:13:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8e443315-9659-3443-85c7-7cf279e247da | -13.16264 | -43.09595 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 938af2d1-208e-3cb4-8a61-dbb787608667 | -14.27802 | -41.49558 | 2026-10-05 17:13:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2b52d5aa-3ca8-3760-9ab5-bcef01c00986 | -11.82596 | -47.36025 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 44e33687-81ec-3a29-b6f5-2d26a9cc167b | -10.96242 | -45.39854 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b58450a-df94-38a8-b00b-bba863a09d43 | -15.14635 | -42.16209 | 2026-10-05 17:13:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 99740e9d-d859-35a7-b855-544ee6a77623 | -10.95138 | -45.41669 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c41b25c7-5471-3807-af78-f4f471dc0c41 | -11.95299 | -40.64184 | 2026-10-05 17:13:00 | NPP-375 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e2df1499-ae1a-375e-9503-780a36b32da5 | -8.43362 | -39.54632 | 2026-10-05 17:13:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ec818365-63ad-3ac4-8764-dcb55dc70e43 | -11.29382 | -48.44194 | 2026-10-05 17:13:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 983d0ee6-c4b8-3efb-bc1a-c3e43250406e | -10.96417 | -45.40823 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a319c298-fc96-3cd3-a52b-9df9804461f1 | -15.56947 | -40.92841 | 2026-10-05 17:13:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0b29e067-09bf-384b-8c7e-4401ca7e94d0 | -11.71833 | -43.50461 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6c457d20-8db2-3fad-ab91-58977d9a9850 | -9.84191 | -47.01045 | 2026-10-05 17:13:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dbbd3dc3-7749-35e1-a44f-20ddf69e4562 | -11.63936 | -43.60318 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3ff13c9-9431-3b90-92df-abe2d6f87907 | -14.79326 | -41.5612 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README106.md)
