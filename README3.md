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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8af2d472-6f57-3390-bcda-f8f60dbb19b2 | -10.68672 | -37.11965 | 2025-12-10 03:17:00 | NOAA-20 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a13fee7-6d09-3638-8d8a-9094e4603e29 | -10.68212 | -37.11872 | 2025-12-10 03:17:00 | NOAA-20 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bcf79537-8722-35b1-ae34-21e46bd14ed3 | -3.43147 | -41.66006 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 02a0c452-df8f-3198-b866-7ac6f89c0357 | -3.39055 | -42.11001 | 2025-12-10 03:17:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57f73652-6044-3b36-be3e-d2e064218f9e | -3.42228 | -41.66495 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 50b0ca4f-8850-3344-b8c0-b1d4c87f2678 | -11.10853 | -40.27862 | 2025-12-10 03:17:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d893a664-65dd-32b4-a7da-91c55393d438 | -5.35283 | -38.06366 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 75402964-fe95-3fb9-a21a-891e69eab6ec | -5.35764 | -38.06805 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4b3a0475-9801-3e5d-9db3-4787d52f54f8 | -3.57729 | -41.6741 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9b57933-7e76-30db-9cde-4129064e1d2d | -10.17864 | -36.26775 | 2025-12-10 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee167308-d84e-326f-a23f-39ddb439e9aa | -11.5959 | -38.20077 | 2025-12-10 03:17:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35644e26-87b5-3bfb-85e8-914715109d83 | -10.01031 | -36.39692 | 2025-12-10 03:17:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e1699038-9a50-3061-b77e-62d71343a06f | -3.57838 | -41.67249 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 82c8c28e-f2c2-3e58-9e3b-8addcf75bc94 | -3.39767 | -42.11132 | 2025-12-10 03:17:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 705d51bb-c102-330b-bf6c-0d7a613aae9e | -3.57848 | -41.66739 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0f4cf60a-b028-3622-a799-b1880242c66e | -5.35482 | -38.06378 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c13adfdb-5f97-333f-a23e-acc4a1dd25c9 | -8.70042 | -35.38616 | 2025-12-10 03:17:00 | NOAA-20 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3497a625-f8b0-3beb-8860-190b6e532dbb | -5.35223 | -38.06712 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 13390c01-0afe-32bf-9f6e-437fb24a8b01 | -9.08239 | -40.8818 | 2025-12-10 03:17:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d011cbdc-484d-3e41-9d33-ff7927dba3c9 | -3.58529 | -41.67385 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6882b111-e30b-31ec-9362-873976fe1acb | -11.11108 | -40.27923 | 2025-12-10 03:17:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 55381988-206d-3364-b7a7-ea545bb7a21a | -5.36023 | -38.06466 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 116084ef-85ab-35d0-8206-69e9c7b882b3 | -3.4234 | -41.66536 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2d1b14a0-6a72-3046-a680-cc1a72797a27 | -3.43954 | -41.65474 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f5753c47-5b83-39bf-a653-d630938c0edb | -5.35421 | -38.06723 | 2025-12-10 03:17:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 57cea78b-3ba1-3b8e-bb07-83742ebf1668 | -3.42453 | -41.65879 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 21a9a0a8-882e-3bc8-9bc0-fae9667daa2e | -4.16753 | -40.71269 | 2025-12-10 03:17:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20f3f78a-e0e3-309a-9735-eb4a86bc89ff | -3.39373 | -42.10968 | 2025-12-10 03:17:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f5d1f645-5885-35a2-a668-9da301af4ecb | -3.42346 | -41.65841 | 2025-12-10 03:17:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 21fafeac-e033-3d8d-95fc-37da178a0a24 | -6.60247 | -39.5364 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 117e75dc-8ee9-381c-951a-6c63c205f349 | -6.89066 | -42.84441 | 2025-12-10 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 760dba88-055d-34fd-8cce-9ce24d2338f3 | -6.89702 | -38.10314 | 2025-12-10 03:19:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30673faf-9fe0-38e4-82d7-36f13cd281a6 | -6.60294 | -39.53039 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74be3ecb-2671-38ae-8578-4af82e0b32bd | -6.60789 | -39.53608 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3124b614-de49-300a-b05e-295dc22f4382 | -7.55097 | -37.49863 | 2025-12-10 03:19:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48f98b44-fd4a-3185-974c-c18dd2c7c460 | -6.59734 | -39.52816 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e27b4596-cb70-36ca-b0e2-5e85fc50829a | -6.6032 | -39.53226 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bffd4276-3725-3bed-aece-233a8c9ab40a | -5.99876 | -40.37638 | 2025-12-10 03:19:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6a50a58-a31e-3a8f-b539-d00c24213686 | -6.78161 | -38.33049 | 2025-12-10 03:19:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 002a7672-28b4-36c0-ada7-5d83cce5a45d | -6.6014 | -39.53872 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03cc497f-3b2e-3f4d-a8f7-8bd584c50088 | -6.0041 | -40.38225 | 2025-12-10 03:19:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4abdabef-e757-3f32-a64f-5a4a11e272d0 | -7.29046 | -39.00629 | 2025-12-10 03:19:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 631afd7f-450e-33f8-9ebc-f7ce0a756df9 | -7.28978 | -39.01001 | 2025-12-10 03:19:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1abe4a94-198d-34c2-b20a-ec9bb7040fc5 | -6.90285 | -38.10096 | 2025-12-10 03:19:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50558386-f5eb-385b-85e2-ca164c4a49e3 | -5.67054 | -39.60296 | 2025-12-10 03:19:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86f15459-0f38-3ec2-85c2-202256125e65 | -6.06908 | -40.01798 | 2025-12-10 03:19:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b68e6cfe-ad5f-36d4-8a5d-6223f34a72a8 | -15.46092 | -39.15916 | 2025-12-10 03:19:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3b92882b-4787-3bef-858e-5996f2b5d602 | -6.94199 | -38.60976 | 2025-12-10 03:19:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3caa9d0e-b37f-340a-af5b-8feec684249e | -6.94741 | -38.6109 | 2025-12-10 03:19:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd3048c0-47f6-3f1e-a169-744392cc3acd | -6.94138 | -38.61324 | 2025-12-10 03:19:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2911579-98a1-3342-9366-8c1b5f49b481 | -6.00497 | -40.37735 | 2025-12-10 03:19:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4bd5ff6b-3f05-3543-9cd2-cd0522081610 | -6.89772 | -42.84566 | 2025-12-10 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| faf4476a-6a8d-3633-b67a-5d71583ea332 | -6.60217 | -39.53452 | 2025-12-10 03:19:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| db223dd1-7ecb-3a09-a1c4-79103cb1bfce | -7.55149 | -37.49575 | 2025-12-10 03:19:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cbcf6e8-30ac-3146-9eae-493618de92cc | -5.1749 | -43.1224 | 2025-12-10 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bf103e9c-1b3f-3da3-8275-ff69f516e984 | -5.1749 | -43.1224 | 2025-12-10 03:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 264711d9-6d18-3cf4-b9f0-00631850acac | -5.1749 | -43.1224 | 2025-12-10 03:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9d28ac5d-1422-372a-8bb2-cc5ab9398a7b | -1.5832 | -54.12372 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c1faf18-2a62-39a6-ae92-e0a331bcd748 | -2.26443 | -47.86731 | 2025-12-10 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4b835d52-9a77-3ace-8aae-2eec1e48cc52 | -2.36875 | -46.3145 | 2025-12-10 04:06:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e94c721-0d60-3594-bf60-cfe00a211331 | -3.6386 | -40.94663 | 2025-12-10 04:06:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb94e74d-e669-33e9-9528-ec08178e1409 | -2.28737 | -47.94593 | 2025-12-10 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0c973c3-dd42-3194-ad9a-72b1a4dda96f | -3.35612 | -40.01104 | 2025-12-10 04:06:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a7440154-99ab-3b20-85da-da59ba154856 | -2.02681 | -52.05265 | 2025-12-10 04:06:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e67923d2-895a-3f91-808b-12e94378f4ee | -3.43112 | -41.66016 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8da48d6c-1341-38f6-ab4a-5a515032aeb9 | -2.36315 | -47.68771 | 2025-12-10 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f16bb4f6-13b6-3829-8dbd-e874a5e10224 | -3.9366 | -40.73652 | 2025-12-10 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e907f24a-a4b0-332e-aaef-358a3612ce58 | -3.42447 | -41.65913 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d71c55fa-a178-33f7-9529-056f6d7becf2 | -2.49065 | -47.77452 | 2025-12-10 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72568eda-e4de-3f6d-af03-a865fb1e9cc6 | -1.59026 | -54.12489 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2709cbd3-8574-398e-acab-d900b69bd48d | -3.39894 | -42.46371 | 2025-12-10 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 63285456-1d95-3b05-bdea-83d51bfd1bcd | -3.68297 | -40.72819 | 2025-12-10 04:06:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1323909-523b-3dc6-8794-7be34c222cee | -1.97303 | -45.86751 | 2025-12-10 04:06:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c42a624-f23a-3879-9961-fff5385f825c | -0.84544 | -48.10837 | 2025-12-10 04:06:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26143d4f-f1bd-3c81-a3de-0a6576b6a4c2 | -3.43554 | -41.65372 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8be7c268-dc67-3605-be2c-4dbbc513bf1e | -3.17307 | -43.10819 | 2025-12-10 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95d17f9-5eca-3229-88f1-7ee208eb4f28 | -2.64784 | -46.9609 | 2025-12-10 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac827b1f-1cc3-3981-a84c-3ec8b8c1dccb | -3.58991 | -41.66706 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 58ff1dd5-717c-31a8-b132-b5f980725dd3 | -2.80152 | -47.35814 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01bb1375-615a-33e9-8696-291015487d4d | -2.52325 | -45.02262 | 2025-12-10 04:06:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af8fa992-0b5b-3cb1-987b-cf8f24ea3611 | -3.39951 | -42.4601 | 2025-12-10 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0f5b7d0a-79fb-3e55-8799-8a50c2895260 | -3.4217 | -41.65514 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 63cf1282-df88-3737-b0fd-22a3f0f33c41 | -3.59323 | -41.66757 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ea6f20e-4a66-3014-beba-b52d391c0cf0 | -2.79967 | -47.35611 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a398ce3-767d-3f4a-bb08-740473ea6a32 | -2.42055 | -48.27293 | 2025-12-10 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ce30119-d83c-3321-b73c-e4b92d9f5544 | -4.15968 | -40.65882 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb01f493-2704-3401-b234-6e5090e58d8b | -0.84456 | -48.11378 | 2025-12-10 04:06:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf25c742-f2c6-3a37-a74f-3ccc8cb068e4 | -3.06394 | -40.38055 | 2025-12-10 04:06:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7ef5fa59-42e9-32ba-bb6c-ed2cf74f87c6 | -3.39812 | -42.10812 | 2025-12-10 04:06:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 270ff83c-b92d-3e00-9514-2c62f41f0bc8 | -2.42139 | -48.2677 | 2025-12-10 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69850428-9468-3221-b4df-dafbb5e56237 | -2.02759 | -52.04788 | 2025-12-10 04:06:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b776f903-f360-3d50-a692-35835fb01699 | -2.08245 | -52.05409 | 2025-12-10 04:06:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5816b5ea-9454-3321-b1be-756c0f3b7d77 | -3.39836 | -42.46734 | 2025-12-10 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e7685d0f-e157-3fe7-b227-67873ec18751 | -3.68117 | -39.76027 | 2025-12-10 04:06:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3935fdf-a803-30bb-9cfd-8bf6ea110c02 | -3.39868 | -42.10457 | 2025-12-10 04:06:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| db9aa5fe-771a-3242-b62a-fb6139da251b | -3.74589 | -43.26279 | 2025-12-10 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b6a76bb-be7c-32fc-9d81-2bb152c3d736 | -4.45699 | -38.39125 | 2025-12-10 04:06:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8785ed98-dbf5-312c-b583-d8312aa945ac | -2.26161 | -44.61282 | 2025-12-10 04:06:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c771e6-5669-3784-8b6f-7d51e364f1cf | -3.42779 | -41.65965 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0d34d89-d5b1-3da9-a8b4-02269afea278 | -4.15799 | -40.64793 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
