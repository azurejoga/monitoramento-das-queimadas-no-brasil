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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60677989-18b1-3373-877f-b1970972ff5b | -13.55833 | -47.38716 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74bb08a1-4346-33bd-9e66-e1e64f8e3874 | -14.65825 | -46.55035 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f0823b6-656e-35b7-8074-3ace47effc41 | -12.87396 | -46.44198 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 366d1172-622b-3513-8663-8b33c5d703e6 | -13.27292 | -47.3077 | 2025-11-16 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 067a1f00-f498-36d4-9892-3288e7c61d25 | -14.64798 | -46.58821 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2cb751b-90be-31b7-90a4-71816e33fb47 | -14.6789 | -46.55896 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07830672-3bd8-326e-80a7-3585f3622f12 | -16.49846 | -43.73555 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61220cd5-1361-3334-b455-9d27c85967e7 | -13.8145 | -42.54884 | 2025-11-16 04:10:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 885b0255-a1b5-3fe2-bee8-70948ed1a6cc | -14.67469 | -46.54061 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c37c7d46-ed9e-3c79-925c-273d31c87929 | -14.64518 | -46.56185 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b51ae491-dc1d-3fb6-a37c-efb1b2467fbc | -13.75615 | -48.671 | 2025-11-16 04:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6221384-624c-38dd-888d-ca84186cc668 | -14.57899 | -45.21973 | 2025-11-16 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73a3abf4-dac6-3d25-94b1-1d5731e984ae | -16.53151 | -43.56817 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f37bdfb-3580-3b55-8ed5-ff918f667b61 | -13.58574 | -42.99199 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c6d7990-6184-3e37-aaf1-4c98eadfc91f | -13.36491 | -44.05816 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 356cc99a-415a-34c5-8bb6-e9599eeeb57b | -13.55847 | -44.10087 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a1dd37c-c756-3591-912c-0aaa8f47938e | -16.52876 | -43.56403 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5608a8f-d437-371a-a49b-a72822a58a84 | -14.05712 | -43.1273 | 2025-11-16 04:10:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1af1343-6e19-31b6-9364-a0992314d74a | -16.5658 | -47.60914 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63d082c0-7d8a-3162-ac07-a07abab4627b | -13.55739 | -47.3925 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aad38426-d8c3-313f-8c17-5b8691c787f2 | -12.67567 | -47.16673 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27aef8ac-2b2c-3de3-aa0d-f6644a115c47 | -15.46128 | -39.23993 | 2025-11-16 04:10:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 407555f4-a28c-3725-8981-be642c168c64 | -14.64382 | -46.58143 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf48179c-6273-31b1-b90f-ba91f366f9a4 | -14.64147 | -46.58314 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f2708e2-dd9e-358b-8d97-3e3ecb7999bc | -13.71022 | -43.66543 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29d399b9-0ff8-3749-ba2d-95726b8a2f36 | -14.64671 | -46.56428 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14d61826-9841-3a14-8265-a38c51ca7e82 | -14.64073 | -46.58737 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31095365-9b64-34c8-9c02-7a7c6551483c | -12.67026 | -47.17549 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e10a19fa-8d21-34ac-a577-65d4f65a2bb1 | -12.809 | -46.44885 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0157657-ca2f-3a33-af61-026f1ea7b665 | -13.97962 | -48.77953 | 2025-11-16 04:10:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d69f20b-c18f-3d81-b056-a9289410467e | -12.85634 | -46.4573 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e289298-d2f5-34f5-b2f5-24cc88a8c296 | -12.87536 | -46.45581 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2e8347d-2d81-3ec4-a2cd-8138dbecb994 | -15.47106 | -43.18359 | 2025-11-16 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b53c06d7-0487-3949-a450-5a6872eaac71 | -14.65014 | -46.57579 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d2ad260-85ac-353f-9798-e9a09e57db39 | -13.75202 | -48.67044 | 2025-11-16 04:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41bfc67-117c-3a3c-a897-ce7f6b0ae9a2 | -14.64312 | -46.58559 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74eaf70f-4f93-333f-bfa1-22fd7733c91c | -14.66756 | -46.53916 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9918a3a2-a95b-3b9d-8365-513d9ae426fb | -13.55431 | -44.27439 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44b1db00-c113-3d40-89ab-22d0b378b9cf | -12.85138 | -46.4207 | 2025-11-16 04:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e804da19-a595-312a-b15e-ffb5b98f7133 | -13.71353 | -43.66598 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0862fa0c-7290-385e-a33a-d13796eab061 | -12.67107 | -47.17075 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22d83dd2-9f5d-3799-aa47-5063f9d53d26 | -14.64239 | -46.58991 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1c33cb6e-de5d-34c4-b51a-8eb1979efb26 | -12.66727 | -47.17007 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cae4b0f-8388-36d4-a7bb-9eeefe5566ad | -13.7141 | -43.66243 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11aba8a5-47eb-398f-8b65-3e4f9d9a1c7d | -13.71136 | -43.65833 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 196d1ed5-ffdc-3466-bf33-26930ea66ec4 | -12.95446 | -48.81726 | 2025-11-16 04:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 422a891f-9596-352c-abb2-d89b2c1db056 | -12.85715 | -46.78555 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f4c921-c03f-3c8e-b063-1991cc761009 | -14.68035 | -46.55052 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c06c61c2-9612-3d64-b375-d8d3cd8d8956 | -13.38765 | -44.37676 | 2025-11-16 04:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877f1a83-a63f-34e9-96b6-993aa38248d8 | -14.67537 | -46.55804 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d60cba5f-4317-34e9-a185-66208c4b6053 | -16.51502 | -43.5433 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 403b1910-0061-3607-bacb-ec67113288b6 | -15.48075 | -44.1958 | 2025-11-16 04:10:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 583ce0f4-6028-3afe-8f39-726642d11537 | -16.56212 | -47.60847 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb8dc190-d4d1-3cbd-9918-49b9153e7bef | -15.52534 | -45.7582 | 2025-11-16 04:10:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7a29e74-2ce9-305d-bc3f-6744783c7505 | -12.87686 | -46.44698 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 126b913c-24d0-3775-9089-6fa3b1f651e1 | -13.86652 | -46.84807 | 2025-11-16 04:10:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53f7cb81-64f7-31c9-b99e-6d01919f23c5 | -13.05466 | -53.95145 | 2025-11-16 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f9ffbb1c-51fb-3401-b3fa-975ea1c98153 | -13.26908 | -47.30734 | 2025-11-16 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b57eddd7-66e0-36f9-96e4-8e8a0dc29148 | -14.89863 | -47.37259 | 2025-11-16 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19ed1c44-da5c-3a7f-a1bf-e3c5a0cfadf4 | -13.40653 | -48.52277 | 2025-11-16 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89f0dea9-c8c4-3d89-bab5-2626fde97220 | -12.67323 | -47.18097 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dedd2cba-7176-3a93-a581-1f6f2b26ef38 | -13.30707 | -44.26654 | 2025-11-16 04:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e60eb247-1581-3e88-a44f-fc96611a0c82 | -13.55706 | -44.27858 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ffab2bc-da20-3602-8559-97a64fd74a7f | -16.1407 | -43.65723 | 2025-11-16 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa2e2cec-002b-3160-95bd-264fb489bb90 | -13.8238 | -43.91065 | 2025-11-16 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8448d096-326b-34da-8646-d959c809ffe3 | -12.80507 | -46.4493 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 465a1f48-63b4-3b3c-b76f-591bedb8d0c9 | -13.55514 | -44.10031 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4079e691-7f03-368d-b290-0af19300dd77 | -12.85344 | -46.45234 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f17647-9349-3dab-a77c-7e1e6118acf0 | -13.71467 | -43.65889 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 516234e0-7cdc-3b17-86de-43549f31dfb2 | -12.66944 | -47.18026 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e49ecd0f-71e2-3975-9f28-b05b8310edca | -14.20534 | -41.84261 | 2025-11-16 04:10:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0384b9c3-11cb-3ccc-af16-3461c6812eb1 | -13.73521 | -49.79204 | 2025-11-16 04:10:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ede9208-d089-3944-87e7-fd35e548b374 | -13.37812 | -43.59595 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f42e683-c471-3e6a-8de7-461e92d72996 | -12.7971 | -46.45203 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf95dabe-2ce4-38a6-83d3-3eab0a4569f7 | -12.66646 | -47.17482 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ed91667-43f7-3d31-9ad8-bafb88915967 | -14.57577 | -44.13928 | 2025-11-16 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dd82fc00-9240-3026-a753-e980e37f1c05 | -14.64727 | -46.57102 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe9f0df-d5fd-3c9f-918c-c6bbf8a06808 | -13.39938 | -44.14151 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03394049-d1b2-3b1b-b5d7-3afa0c56f7a6 | -13.0564 | -53.94945 | 2025-11-16 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9e36775f-4dd3-3c8e-8788-b34d40ab726b | -13.82635 | -43.19079 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa5356c7-1dfc-3571-973e-bfe6fa32e2e0 | -13.81464 | -44.44862 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4452e746-64e1-3c6f-b6e8-ba3aa835eb0f | -13.81506 | -42.54527 | 2025-11-16 04:10:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 95207f68-facc-3e35-8409-78f012482564 | -17.05076 | -44.04564 | 2025-11-16 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9defdfca-d240-32f0-a4f8-932d15e31325 | -13.81858 | -44.44555 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6634456-132d-36e0-8382-0be9474f60cf | -17.14715 | -47.31764 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75d6210c-8947-35fb-b78c-56ed86cf40ae | -14.65391 | -46.55408 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 161e7f41-d707-38af-83fa-1206a1bdfff3 | -16.53207 | -43.56458 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05b144ef-7454-32ed-b6a8-5a1698e2eea3 | -14.67824 | -46.5414 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 492fbf1c-5d47-3292-bb60-603af35500ac | -16.14401 | -43.65779 | 2025-11-16 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee58159f-670f-3755-9654-af78bc9056b6 | -13.55038 | -44.27744 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa8cb0e9-428a-3e0d-8aae-cdfdf8093497 | -13.35421 | -43.63926 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1cb7d1b-cf9e-3bcd-bfd7-43c7bb834f93 | -16.56661 | -47.6046 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68978cfe-a36f-3277-ad15-0890fc2b6135 | -14.15594 | -43.40448 | 2025-11-16 04:10:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca7f9d1d-8582-3992-a0c6-8847a6f96bba | -13.71079 | -43.66188 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e25fe96-8767-3edd-820a-31367d18394e | -12.87611 | -46.45141 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37f189d2-ef62-32ff-a050-569df2ebb2c8 | -13.30648 | -44.27018 | 2025-11-16 04:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd6c548a-0ebc-3825-a243-ba18263bb11c | -13.8223 | -43.7715 | 2025-11-16 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 842f0ac0-ae62-300b-94f5-1e8a64a5a88b | -13.97891 | -48.78344 | 2025-11-16 04:10:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faebc9c1-6b95-362a-958d-c72adb3bd321 | -13.75131 | -48.67438 | 2025-11-16 04:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecd723a8-d351-36c1-b7e3-71012e4c3c94 | -14.67045 | -46.54379 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README47.md)
