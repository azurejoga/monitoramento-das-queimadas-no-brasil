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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9faf3cf2-0384-3fd7-9471-efb8b2f7ba02 | -11.7504 | -48.38227 | 2024-10-13 00:37:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 66d8354f-c404-3307-b70c-3baf322ec4d1 | -11.74266 | -48.37215 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6eab8219-8e3f-37fc-83a3-69d5e5eb884b | -11.74835 | -48.365 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a59ec0e7-47bb-3c58-a42e-99dcf88f1620 | -11.7364 | -48.36657 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7cda4d2a-0bce-3fdc-8a0c-673e619701df | -11.64143 | -48.39058 | 2024-10-13 00:37:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 09b9dbb5-a2d7-3fe8-8661-c4b0df3e77ab | -11.63927 | -48.37339 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 542dc26e-ad54-3001-a991-faeb37758dd2 | -11.63506 | -48.38578 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c201cdd8-ef6a-3f4b-848d-90b3d9f6bf19 | -11.63304 | -48.3686 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| c3c2c47a-7915-3288-9c42-0e2498d829ea | -11.62947 | -48.39203 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0d232e77-671a-3771-96e0-8b3243d69dcb | -11.62733 | -48.37488 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 87bb2745-3b7e-3744-979d-1bbd74f3cc63 | -11.59202 | -48.48438 | 2024-10-13 00:37:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 4f563e7f-5763-3ad2-aece-767e8657806c | -11.26684 | -50.9121 | 2024-10-13 00:37:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| cf23e070-c0d3-30c0-b9ee-739ab01b1c63 | -11.25226 | -50.91378 | 2024-10-13 00:37:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 98c7db71-5e38-3fc3-a035-93a4942febff | -11.20658 | -47.85478 | 2024-10-13 00:37:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5a236e1c-ddc8-350b-8bdb-d7272d637962 | -11.7283 | -44.55566 | 2024-10-13 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e9687b9c-b98a-3e5f-93a7-389ad4babfaa | -9.80538 | -36.16481 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| c593935b-6ec9-38f4-b9cd-eb2320f72a49 | -9.80187 | -36.14279 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 1b468ec4-bd43-354c-9377-7242a9ad2302 | -9.80055 | -36.15916 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 54ef6f77-6ccd-3d00-8448-431deb99edb9 | -9.56411 | -44.47295 | 2024-10-13 00:37:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f4a9f8a0-77ab-3643-ab11-98fb56eb61b6 | -9.44723 | -44.15211 | 2024-10-13 00:37:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5cbee054-2b9c-3fdb-9dcb-d040a90792ec | -9.446 | -44.14304 | 2024-10-13 00:37:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ef9d2a4b-85d6-3dbc-b9bd-a036f4300d94 | -9.43681 | -44.15021 | 2024-10-13 00:37:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ce4a0481-da6f-330d-925c-3d9d6abd22e6 | -9.30456 | -35.60306 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| f7e247f1-0103-3463-a9f6-47fc46037929 | -8.86479 | -40.88122 | 2024-10-13 00:37:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 075b1dd5-2772-3961-b097-94c45a65d35f | -8.86327 | -40.87078 | 2024-10-13 00:37:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 21.6 |
| b721ed78-96fb-3bf9-91d4-de6c6d729952 | -16.05796 | -42.27274 | 2024-10-13 00:37:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 582df5bb-ec02-3648-9e16-494aec45ba5f | -14.57872 | -41.70258 | 2024-10-13 00:37:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 985bc417-f786-3794-82fd-0751e68891d1 | -14.18891 | -44.31981 | 2024-10-13 00:37:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 441fc930-6d16-33c2-be33-4df5c8541efb | -14.1876 | -44.30975 | 2024-10-13 00:37:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ac5787b-b7a2-37e1-bc89-528a0ad6b75a | -13.94301 | -44.2592 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f8f85d0b-10c6-3161-b7c0-826982d88fce | -13.94169 | -44.24926 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 028d21a7-a314-3777-886b-01f752596e55 | -13.86294 | -44.42019 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56af3ae6-4fb8-31e4-af4a-5407165e346e | -13.86161 | -44.4101 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 62a6d2bf-7c68-36d3-a7c9-763299619907 | -13.79138 | -44.23535 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 680aa042-0173-3ca8-9ada-78512dfb34ef | -13.78931 | -44.34411 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e00ba37-f221-3fad-9638-ac51a85dafb2 | -13.7838 | -42.541 | 2024-10-13 00:37:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 10fad85b-7727-3bd5-be4d-40a2bf355ee1 | -13.78002 | -44.34547 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e8efa4ea-8d0e-3209-9c8c-3fda9fd62e11 | -13.69075 | -43.88696 | 2024-10-13 00:37:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50175147-9650-30f6-9e85-0e8ca33063f2 | -13.65859 | -43.10153 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cd22154d-b272-3add-9588-f4ed83eaa877 | -13.65733 | -43.09235 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a1521bfa-a9b9-34b0-8fde-33be02268b0c | -13.65347 | -44.22676 | 2024-10-13 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fe8d6ce0-5d99-318a-ad4e-3f8d8a72301c | -13.64968 | -43.10283 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 33b78a47-8968-3ebc-93a6-365bac847c91 | -13.64843 | -43.09364 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 58b73f83-cf3c-3a38-ac07-b1a8a14a93f4 | -13.51289 | -43.05082 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e9eff02b-918b-3b10-b3f5-815c1c6576d3 | -13.46836 | -43.66918 | 2024-10-13 00:37:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 15691366-9511-3705-addf-b403d95bfc41 | -13.46709 | -43.65976 | 2024-10-13 00:37:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 58ece308-52c3-35fb-90d7-5c613307fd7b | -13.45933 | -43.67047 | 2024-10-13 00:37:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80efc76c-95bb-363e-8d0c-5851ae65f5ab | -13.45807 | -43.66105 | 2024-10-13 00:37:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fb361472-d9c3-34e9-9fdf-7efb4c1ac5d7 | -13.32877 | -43.18337 | 2024-10-13 00:37:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8071e93f-d96a-3b93-9e78-0f28fd42e773 | -13.14235 | -41.97226 | 2024-10-13 00:37:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 15119c76-3247-387c-b5b2-8f22dcc45bfb | -13.14106 | -41.9632 | 2024-10-13 00:37:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 85498ca7-acbe-3e02-8ad8-7a54ed7518a8 | -13.03943 | -39.93305 | 2024-10-13 00:37:00 | TERRA_M-M | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 89fecc76-9577-3663-8c28-af026ab99cc1 | -13.03782 | -39.92225 | 2024-10-13 00:37:00 | TERRA_M-M | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e8af26ce-df76-39aa-8500-7d36e98c076f | -12.98518 | -41.51627 | 2024-10-13 00:37:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 7678a43e-3e67-36de-a5bf-9e0a44cca92a | -12.98385 | -41.50702 | 2024-10-13 00:37:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a0fc02ce-b29b-35e5-9619-7d1d466880a0 | -12.82646 | -41.18246 | 2024-10-13 00:37:00 | TERRA_M-M | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8d97b6e1-721d-32fd-9ee2-9abdc130e104 | -12.723 | -40.22072 | 2024-10-13 00:37:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| eaee6370-2ccb-38c8-bc72-a80bb09accee | -12.67439 | -41.46881 | 2024-10-13 00:37:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d5ef515c-7d2b-30ea-92af-8b10a90b9dde | -12.37088 | -41.60474 | 2024-10-13 00:37:00 | TERRA_M-M | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 25b9bb50-510a-314b-b1f5-fd2c4e94ca1e | -12.28602 | -43.84034 | 2024-10-13 00:37:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c42159f6-854d-3525-9840-36fc2db5ab02 | -12.28476 | -43.83101 | 2024-10-13 00:37:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a2742c4-f6fe-3aff-a522-f638861ed821 | -12.12286 | -41.41747 | 2024-10-13 00:37:00 | TERRA_M-M | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 902d338e-0c80-38b4-911c-22b4f7461e66 | -12.1214 | -44.74791 | 2024-10-13 00:37:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b266e30c-9dbe-3d6a-b56c-3c58878d510b | -12.12009 | -44.73788 | 2024-10-13 00:37:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| db91ea29-0b33-3a40-9924-b5449dfc57ec | -11.9296 | -45.79502 | 2024-10-13 00:37:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 494a6678-95b0-3e96-8760-2150297fb617 | -11.84152 | -45.12408 | 2024-10-13 00:37:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6b99a0f4-5a25-3dcf-824a-cc46ed9cde80 | -11.72701 | -44.54589 | 2024-10-13 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85840c7b-3257-3411-982e-e5b65436b10e | -11.72571 | -44.53613 | 2024-10-13 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b721d38f-b601-37dd-b30e-c10eb3deb566 | -11.65191 | -41.73423 | 2024-10-13 00:37:00 | TERRA_M-M | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1ac9f1ff-37d0-3b7e-8916-7de429600d76 | -11.46038 | -43.92828 | 2024-10-13 00:37:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f878efe9-0b4a-382e-bb7e-d8cbd2415922 | -11.12772 | -44.95333 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c390f8f7-d695-309e-8372-11301520a847 | -11.11253 | -43.33659 | 2024-10-13 00:37:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| dcac74b4-2cb6-31f9-95ab-650387a00cfe | -11.04703 | -42.01824 | 2024-10-13 00:37:00 | TERRA_M-M | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 3169faa0-8f53-32e8-8baa-2719678e8595 | -10.95833 | -44.63877 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b7c771f4-c201-3776-a0e3-702b2b939ed8 | -10.94389 | -44.67036 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 61c7bdc0-20b6-3f5d-95ae-c8c6b42d8005 | -10.94259 | -44.66068 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b363af6e-ada3-39f9-867f-b0c9a7572573 | -10.9373 | -44.69104 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| df7211d1-e13e-3ed5-8ce9-a69557ca0956 | -10.936 | -44.68134 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 70c8a91b-a3b7-3049-822a-6a13b7e94a7d | -10.9347 | -44.67163 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 34824008-d63f-3f67-b436-d17925091bf3 | -10.89231 | -44.35609 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c7f6cab2-dfec-34f6-9066-9495e48a5cc4 | -10.89104 | -44.34665 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5bf8ba2a-a2b9-3ed7-8019-88096d2c3170 | -10.85975 | -43.64005 | 2024-10-13 00:37:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ea0f9de2-3603-3026-b09e-5420c5a8c6d3 | -10.71879 | -45.05123 | 2024-10-13 00:37:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 18a762cc-9d37-3913-a068-9b6730339444 | -10.71692 | -44.48914 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 141ba6d3-5803-39dc-83c4-dfc383646d30 | -10.70782 | -44.49036 | 2024-10-13 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 99c543dd-769d-31a4-a50f-245cf6b7bfd0 | -10.50982 | -42.51385 | 2024-10-13 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 98b20ad4-389e-3e4e-a86c-cff0ad5ad8ab | -10.50855 | -42.50486 | 2024-10-13 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 756346c2-56ad-3c7e-938f-694aa0b83981 | -10.50018 | -42.52123 | 2024-10-13 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e48581bb-627d-34d9-8c4e-69ec8391c5ec | -10.49891 | -42.51224 | 2024-10-13 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d9c46191-f097-386c-b3b3-05d01521fd52 | -10.49765 | -42.50324 | 2024-10-13 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2178b626-843d-3883-ac47-8241a8f1277f | -10.44761 | -44.94555 | 2024-10-13 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2750eb2b-0df2-3baa-8455-4c24b586e890 | -10.33162 | -44.97785 | 2024-10-13 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9c972c96-e24c-3b5f-a3a5-336ac5b7c422 | -10.32236 | -44.97911 | 2024-10-13 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1117a422-8135-391a-93fc-a994f22db24a | -10.21278 | -42.44422 | 2024-10-13 00:37:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e81f6f7b-887a-327d-ad61-d1f1afc4ad4b | -10.20094 | -36.42229 | 2024-10-13 00:37:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 77c01273-92ad-35de-a25e-34e199bef0b5 | -10.05794 | -44.1782 | 2024-10-13 00:37:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8fae3bbb-4813-3220-82de-85ba92d6afd6 | -9.95142 | -47.27708 | 2024-10-13 00:37:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8a54ad8b-0160-3085-94ff-64e9785d9346 | -9.9449 | -47.27162 | 2024-10-13 00:37:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cd0ae5e6-6561-3f3c-8513-bbfd9815b784 | -9.82865 | -46.99022 | 2024-10-13 00:37:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1ddb2b6f-7e2e-310c-a9ec-a548fab7b375 | -9.74052 | -48.3016 | 2024-10-13 00:37:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |


[Clique aqui para ver as próximas entradas](README7.md)
