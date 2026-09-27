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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1709f4d7-120f-34cd-9ab7-7aee07cffd44 | -8.3554 | -44.15527 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 588581fe-257d-324e-970a-c0511cea3eb0 | -7.29041 | -43.30864 | 2026-09-27 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5524532d-8459-3bf8-b8e1-c239e2840414 | -7.3302 | -42.08665 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ef8784e7-3a94-36ff-8cbd-ece4cd7e4773 | -5.50168 | -45.51771 | 2026-09-27 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17b39ef9-2acb-39ef-98d1-8bc6541f0c89 | -6.83948 | -43.51576 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb51456e-5548-3ebe-8b49-f37b110ce28e | -5.42669 | -43.44751 | 2026-09-27 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69ae7ede-feae-3643-931d-76de27d3ed92 | -5.73266 | -45.01835 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddb0872e-6400-3799-bf28-df870081d1cb | -5.75717 | -45.29042 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 472037ff-3d2c-3787-a525-22fbd9182cfd | -8.36107 | -44.15637 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 31ffd828-6777-3e5d-9dbe-6e8ee29b3a91 | -8.34386 | -44.18549 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7af2a7cb-4db0-3a6f-9fdf-21c3067a3e52 | -8.35323 | -44.16687 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 26f24c7c-7166-3e6f-b44a-3d15f007d410 | -6.83317 | -43.51867 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20f6d476-fc35-3cd9-9b4b-75dbe960eaec | -7.29031 | -43.30761 | 2026-09-27 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 634aa4de-6491-35cf-8623-ce1f8c9d2363 | -7.35788 | -42.10651 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 603b324a-ff87-3bca-bfb7-6e711924b4e2 | -5.73711 | -45.06506 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa68321c-875e-31a9-aac7-f22eb7322cf9 | -8.35046 | -44.15032 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed6acf84-a4b6-3b2c-bcd3-34a1fe6369cf | -6.83694 | -43.51297 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13625410-13ad-33a3-9cc5-91f9dc5fbd3a | -6.93873 | -41.61136 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a568a97-8c69-3ff7-ab6b-4fd6e273bb90 | -8.34812 | -44.19417 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5f32c038-ad4e-3b91-aca4-9b77b4e7a06a | -8.34259 | -44.16094 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e8a2161-42a1-36ae-bae4-8db649c65aeb | -8.33614 | -44.164 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b0dfd27-6241-3afe-acb8-6783124b9774 | -8.36179 | -44.15252 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e217d259-8e55-3c38-ba9c-5596c7e562bb | -8.61584 | -35.6129 | 2026-09-27 03:47:00 | NPP-375D | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 072ff2fe-4484-3ae7-bfe3-25809e8be7a8 | -5.76101 | -45.29507 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d7fce1-77ad-38f6-8a3b-e8f6258a683c | -7.20171 | -40.12491 | 2026-09-27 03:47:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cf02fa9f-c250-3a82-aad7-691bfc4cc048 | -6.94289 | -41.60991 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b502b85f-969a-3952-8f0e-77f38f48d5aa | -8.3653 | -44.16517 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2b5a9d3-05f7-33da-bf21-551a33066947 | -8.3411 | -44.16888 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| addf4f9b-f4f6-329b-b8be-ebf98fb3b0af | -6.1746 | -44.59444 | 2026-09-27 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cacd1e19-59a9-332c-b53f-b07d57ecaf80 | -5.43305 | -43.44467 | 2026-09-27 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a70ad34-6059-35c6-9ec0-6fb1e0b84fa1 | -8.24974 | -43.78508 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f02fa66-7d09-3449-b0da-4bcf5f63b24a | -7.3589 | -42.10076 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17c1187d-a44c-3e70-bd0f-95680f3bc09f | -7.36087 | -42.11904 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42a0b1e0-b425-3948-b99f-3d527f3065f7 | -8.35468 | -44.15913 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| cbe074c7-8df4-3ea0-9a9f-27fbb1ffb06a | -5.76191 | -45.28997 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 147bacd1-f34f-397a-887b-94b863a825a9 | -5.75555 | -45.28883 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9aa34974-95c9-3ca2-8fff-a28417b4e2b7 | -6.94459 | -41.60697 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a74b87a9-4d5d-3e8b-9c36-3b19c3a6b022 | -6.84253 | -43.51395 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83afbd0f-fae6-314f-8ee8-31f9e762d2bc | -8.3413 | -44.13657 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 807486f3-71b9-314e-8a08-3c6bd1718fdb | -5.43372 | -43.44085 | 2026-09-27 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f93e52b4-9406-367c-b434-77d558f0197f | -7.66938 | -45.48649 | 2026-09-27 03:47:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c2ab0cb-f8f1-3fcb-8654-de713e548605 | -5.73159 | -43.27746 | 2026-09-27 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7c7600fa-5e3d-3079-8654-cdc1b484bdee | -8.07351 | -40.83667 | 2026-09-27 03:47:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 704eb2e6-2dc8-3e03-8203-0134a8bfe810 | -8.34681 | -44.16974 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16861f62-490f-3f03-8bb0-520d4776089e | -6.84016 | -43.51204 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16a1c5e8-1074-3ddd-ae62-eeb631cfede3 | -6.84318 | -43.51027 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4c5512d-3075-3da2-abcd-999e2a96105a | -5.74334 | -45.06643 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 464fae54-7112-35e5-ac7f-a2bd60d9e3cf | -6.83879 | -43.51951 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 299c55f5-2d10-3c61-8538-be8cdc0c229f | -6.16856 | -44.59327 | 2026-09-27 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82672de6-608d-3de6-aad4-df05fca87703 | -5.50264 | -45.51248 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bde4336-53c7-3776-9176-3531085cd0cc | -6.31276 | -43.33704 | 2026-09-27 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69d972b3-a8c3-3f56-8d5b-026445ed127c | -8.35612 | -44.15142 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 31b38453-0123-314b-b293-201d96c49dbc | -7.34741 | -42.07763 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9f2f584-4c6e-3f97-8151-2c47211817fd | -8.34901 | -44.15805 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89aaaf07-1153-3f36-ab70-edd4431d88d2 | -8.34755 | -44.16583 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c025439-1a74-39be-ba1f-c435d307dbf4 | -8.34696 | -44.13766 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ea507bf-70ba-34a0-8c40-35c92fcf4372 | -8.35396 | -44.163 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 33ef1ceb-d11f-3527-8b86-d0a288d7d0d5 | -6.93707 | -41.61431 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c276285-dafe-3e9e-b344-02d090dcb4e1 | -8.34608 | -44.17366 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b30d848a-7314-3df1-be4a-6f9792fff8da | -6.84084 | -43.50836 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3acd45f5-3a75-3161-91be-08b6d01f4c1a | -8.35601 | -44.18344 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 8594e1e7-0341-31d4-8bdb-189b33f8f857 | -5.73227 | -43.27359 | 2026-09-27 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56e62b7b-39e4-315c-a842-350c9dce4011 | -8.35118 | -44.14647 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d078c045-47f4-3b6c-a8ca-0e1e9e961121 | -6.93775 | -41.6168 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d61fae6a-cb55-3686-8c08-b2b10d88531a | -8.35746 | -44.17567 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 7e617b0a-8a20-35b0-8f5f-f493b9f62f94 | -7.32463 | -42.08873 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fca6e871-d8aa-377d-8e54-f44ec3f3bf39 | -7.36643 | -42.11702 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df2f6534-16fd-39b2-9736-570e20d0651f | -5.75623 | -45.29551 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 73057b2a-be73-3181-bf12-7c2d3da95c7e | -5.73714 | -45.02924 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 235c7237-a911-3e45-bda6-e2ec4d356743 | -5.7318 | -45.02306 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f00f2251-c547-3b64-b8e4-b9d419bc35a4 | -8.33538 | -44.168 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e13adb9b-1b00-30fb-bdef-fa3e55998617 | -8.35891 | -44.16795 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 0f646c91-0338-3b7d-b8fd-b921856ed7d5 | -8.36458 | -44.16903 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abfd76d5-2501-3ba4-a550-c2d54e340667 | -10.10298 | -36.2839 | 2026-09-27 03:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 946a6183-fe9b-3692-9ff5-431a06322f43 | -7.37354 | -42.10624 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f5587ba-6116-3de2-b2c2-9b856ce03870 | -7.37251 | -42.11208 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| efe9cb28-fedb-3cf6-a2e3-5fc0e9487876 | -5.50293 | -45.51105 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536e9873-1e2c-308a-95da-9e0c3c7bfe36 | -7.3469 | -42.08051 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b687ac89-d76f-3006-85a5-785bb72ffdd2 | -5.18228 | -46.1177 | 2026-09-27 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 804422ab-1f3d-38c8-8fc4-630b00228b34 | -7.33472 | -42.09047 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6f21fbe9-47b0-3672-9882-3081e6777288 | -7.32967 | -42.0896 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 485e8f68-3882-3bf6-a1a2-ffaa8f6b6bbf | -3.46359 | -39.58462 | 2026-09-27 03:47:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa831522-e969-382a-9a0b-59d0153b8229 | -6.16776 | -44.59774 | 2026-09-27 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 831bf1aa-4bf6-3ea4-a93c-67a5689941bf | -8.35455 | -44.19126 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b508c813-1933-3051-bd70-de3bcc25d17c | -6.31439 | -43.33793 | 2026-09-27 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c13be3ee-120c-3362-a42b-3f8a11c3c54d | -8.34185 | -44.16489 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52769349-ef21-338c-b382-aa2750a0d547 | -5.73891 | -45.01956 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef908a74-0bc4-391c-acf1-ad697c1a5014 | -6.83479 | -43.57292 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ab8716-a7e3-3a59-8a7e-b7989c591f12 | -6.31208 | -43.34077 | 2026-09-27 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12b17a18-9944-30f2-805a-194a2d7a200f | -7.29097 | -43.30405 | 2026-09-27 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b4bbe59-557f-3440-b028-0b6912ca3ea3 | -8.34884 | -44.19031 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0f7b375f-1d90-373b-aa63-5dd65ec235b9 | -7.35245 | -42.07851 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5da98026-d3cc-335c-9d60-67026e731367 | -8.33425 | -44.16467 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a1852f2-18e5-398a-8357-2a424ab4d079 | -7.3363 | -42.08162 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3c410e54-5643-3667-b78d-70135b5c52d7 | -5.73804 | -45.05991 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28e5c08c-b99d-3624-8c31-bcb3f2a1d9e0 | -8.07808 | -40.83746 | 2026-09-27 03:47:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fbf7286a-72c3-397e-8c67-9de6aeaa4d2e | -7.35981 | -42.12503 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f598d199-b547-3e05-a6a9-fac5c93f1901 | -7.20247 | -40.12047 | 2026-09-27 03:47:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 08add8c8-9c75-3338-a752-9e998d1fce1f | -7.37148 | -42.11795 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93619605-c9e4-3ffb-ba40-6ec619505762 | -8.33961 | -44.17677 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README11.md)
