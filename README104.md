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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c540305-a320-3cfd-8798-f8425e72d347 | -10.94387 | -60.98091 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9728a3ad-3e09-3ead-ab23-f26e1fdce7d3 | -10.94318 | -61.10153 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a767a1b-6354-3617-b4ce-c4368b835718 | -10.92203 | -60.96195 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 642e38e0-6dae-3767-9e3e-ece2d7959fc7 | -10.92017 | -61.34682 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c678a57c-8f5a-360d-a24d-dc165403c645 | -10.91962 | -61.35053 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 899d4bc4-6786-35fe-90e6-5c803aa7f387 | -12.15279 | -60.75249 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c60a8241-10fa-30be-a412-b84b2cf1dce7 | -12.1522 | -60.75651 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98a146ef-196f-3b73-8f31-6fd707be486e | -11.36662 | -60.57478 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efd476b1-a560-3582-9fd5-5caec7073dd4 | -11.35487 | -60.55664 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74aa3f73-6201-318d-96fd-87d78a0dda50 | -11.34322 | -60.53511 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81cd40f8-f1ca-3094-8293-51747864ca96 | -11.33969 | -60.53464 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a65b17-0697-3597-a13b-b3493dbb4479 | -11.33909 | -60.53863 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22d87363-bfe3-304f-9915-5e0204ed86ba | -11.32147 | -60.53601 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23625c7c-4ff8-3900-b535-9626b1c2efc0 | -11.31384 | -60.5389 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac563b44-9687-3b5d-ad76-f27137b5efd6 | -11.31325 | -60.54288 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2963894-b9b8-329b-aece-28111a471b33 | -11.27509 | -60.50841 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a395165-ad05-3ecf-b8f7-60cfc20f4608 | -11.27156 | -60.50792 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2234b529-7ff0-382e-ba3d-c6cd7bb0e8e2 | -11.24694 | -60.55091 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da29dfb5-20e8-39f3-a88f-970b8cd6c080 | -11.24343 | -60.55032 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1046a8bf-9635-3ba3-805c-0606db392bc1 | -11.21586 | -60.56641 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8d877d-39fa-3bfa-a8e9-087cc1d995e9 | -11.21353 | -60.5579 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 758b9805-0d21-3da3-acbb-1879b63ac88e | -11.21294 | -60.56188 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10e5c722-9345-370d-bb3c-4d24859ecd26 | -11.20055 | -60.62095 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a02d54-98c8-352a-a3c2-088c56a17d57 | -11.19775 | -60.51873 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c14364c9-d1b8-3481-831b-58ba70204477 | -11.19412 | -60.61594 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24bfcadd-f040-3274-b53f-61c1b4fe60b8 | -11.19353 | -60.61992 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af2f37eb-e458-3fc6-abaf-52357b831719 | -11.17423 | -60.62918 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fd55098-eb24-3d64-bdf6-3c471156d1fe | -11.17365 | -60.63311 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6bd07c9-3517-303e-a57d-eeeb928c80da | -11.17015 | -60.63259 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0eb8f78a-7106-3b91-ab5d-0bb79fee8dc9 | -11.16723 | -60.62809 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d98f60b4-9764-3a6b-b2c5-6b14cc817692 | -11.16373 | -60.62753 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 314e625c-0ae7-3baf-bae3-af1acefeec62 | -11.16373 | -60.60322 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e74069c-e83c-32d1-b878-633826081864 | -11.15964 | -60.63094 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf93f6b6-4831-36bf-b97b-7ea8e06764e4 | -11.15379 | -60.59764 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3dfaaf0-5da6-37c1-9fe3-6043fe26f6d2 | -11.15028 | -60.5971 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d36adeb-863b-34c4-b48f-a597f3c22ef1 | -11.14326 | -60.59603 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24122be2-2402-3cf3-8c9b-896b57fbeb8e | -11.14212 | -60.6283 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15340c9c-85d6-3cf4-962e-576739c4a6da | -11.13976 | -60.59547 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eec0239-f982-3139-81f8-cf3fa4851388 | -11.09958 | -60.61845 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2f23390-a91b-3001-92db-2b395b5d43d2 | -11.09899 | -60.62241 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b548c282-7f6e-37a1-961d-13e2ec21ed4e | -11.0984 | -60.62635 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbfa446f-76f1-3763-9bbe-81450982e05d | -11.09495 | -60.60149 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d36bd52-dcfe-393f-9964-b354bc62c18d | -11.08437 | -60.64839 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc21e95d-916f-350a-a12b-1878080be2cc | -11.08372 | -60.70061 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c54eb29-51d4-3055-8722-0b46639a42ed | -11.08313 | -60.70454 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf8a835a-8cd8-3328-a6e4-7fd6293d4107 | -11.06567 | -60.72592 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c388bde8-000a-3845-b09e-4f5c3fed7913 | -11.06509 | -60.72982 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebf7bdd-6f3c-37cf-8af2-a7a8d1c86733 | -11.06451 | -60.73373 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1e1282-6ba6-3673-968b-0808b774a0df | -11.0616 | -60.72929 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c3c4ec2-ec96-3b30-adef-d14540912903 | -10.96999 | -60.80773 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd08a97-4759-3928-9e13-75b4866e61c5 | -10.96596 | -60.78726 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fbf6808-3d44-302a-9891-049acfa25113 | -12.15573 | -60.757 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 662792bf-ec1a-3f1e-bb4e-b98c518834f1 | -12.14927 | -60.75199 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9293f655-d6ca-3b89-befa-a5e27b351084 | -12.14693 | -60.74344 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d54103c2-780c-3c3c-9aec-17235d242828 | -12.14634 | -60.74746 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4b20658-22dc-3baf-8865-6d3e2ae7811b | -12.14282 | -60.74696 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32f99778-e315-3766-9ce1-3f045b2b3f70 | -13.73325 | -60.60098 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f1f55f0-6cda-31b5-8160-23117c694f28 | -13.73206 | -60.60945 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bfccb89-c9d1-3472-9f34-3068520a2e89 | -13.73095 | -60.60614 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e88e20c-5600-3352-acb4-c47ff064860e | -13.72965 | -60.60044 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70ef6037-d194-30e5-b9ab-d2f5874ce028 | -13.72958 | -60.64053 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48707de2-3aec-301b-8b57-3e24027d4a51 | -13.72845 | -60.60891 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b952d733-49bb-361a-b3a1-e4e2a92d3a36 | -13.72547 | -60.63008 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 365869dd-5c83-3254-b5f2-98da8c3ac72d | -13.7225 | -60.61354 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f007b83f-05a1-3935-9a58-13076f172620 | -12.33991 | -60.73296 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aceb6dbf-72e0-3829-9fe7-587965cbcf68 | -13.51394 | -61.73496 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e26c19-0f6a-3d67-ba0f-357d642ec343 | -13.51108 | -61.73061 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6203a4b-4982-30ee-9cea-47a08588bfd8 | -13.37748 | -61.94611 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b1927a-b56b-3126-b691-32b8cdea8ac9 | -13.37408 | -61.94558 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b92ce449-d2a8-3b79-b67b-1fe620700428 | -13.29752 | -60.69938 | 2024-10-13 05:29:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4697e2eb-01d4-36d0-a700-dc76f263edf2 | -12.89956 | -60.68359 | 2024-10-13 05:29:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a18c8bb4-e8a6-3a25-967b-25b77e0ecae7 | -12.86405 | -60.50949 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7df5eab-b8fc-38ac-8322-ee5c2abdd488 | -12.86341 | -60.51381 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c008816f-6e26-3ab8-a6ff-f10e5e5e2b92 | -13.37973 | -61.93114 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c469743-6d24-367e-8862-eb5388f182b1 | -13.37804 | -61.94238 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32c48394-4c1f-3b95-9959-e75ad0a89d42 | -13.37692 | -61.94986 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9c23d5-ed67-3028-a7a7-ee56bf4a073e | -13.37352 | -61.94933 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 817392c5-1b1d-31d4-9f3b-79e28f928131 | -13.73266 | -60.60521 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7370bc50-708e-3ced-8a85-55114606a252 | -13.73157 | -60.60191 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bb048a4-4139-30f2-895c-6cbc1a9c228d | -13.72905 | -60.60467 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8695e63-50e7-32f8-a4aa-a699ef5b8e74 | -13.72735 | -60.60561 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c37871f3-97c7-3738-b14f-20e162884c51 | -13.72722 | -60.63154 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca08b2ed-760f-3b31-a1f2-034760807b1f | -13.72672 | -60.60984 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd649d2d-c271-3bb5-b94c-56c981b3f93e | -13.7266 | -60.63576 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f73331d-8618-3ab3-8701-f41e419001db | -13.72362 | -60.631 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 888c1026-8d46-342e-9b82-1e3c08fe81fd | -13.35067 | -60.58405 | 2024-10-13 05:29:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31b5ec72-b041-3528-8efa-3fbff18a1143 | -12.85919 | -60.51761 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a36920a-a3d9-3314-81db-43993904b950 | -13.51852 | -61.75125 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1477ee3-e0e0-3548-94d3-201c2e8d3a6f | -13.51509 | -61.75071 | 2024-10-13 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf95b7ea-865a-3a48-a5cf-9cd383a6d2d7 | -12.1669 | -63.11495 | 2024-10-13 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f140581-3b28-3a02-a80e-1314827b299e | -12.31824 | -62.30898 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c02261c-1a73-3aa0-9167-d83941de1341 | -12.31489 | -62.30846 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33a783df-7fbb-3888-a9fa-7e95bf8528c8 | -12.31434 | -62.31205 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d6e08b-7dd7-372b-930e-62f570798d42 | -11.01125 | -62.59874 | 2024-10-13 05:29:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd33462-3ea1-3660-a3b2-30d6b3d32240 | -12.77073 | -62.27902 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4db293c2-cedf-3b78-a4a3-3b64bca184ea | -12.76848 | -62.27123 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6afca44e-c57f-341c-bf22-60be5e7ca3ce | -12.76682 | -62.28212 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55bb400b-d4dd-32d7-86ed-0ffc25d52127 | -12.76457 | -62.27433 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31ef0300-b952-38e6-a7f8-41e9d3b133f0 | -12.76347 | -62.2816 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1248c3df-3a6a-39c2-acb1-e2d7a17d3fa7 | -12.76291 | -62.28524 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README105.md)
