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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbf20e0e-9fd9-327a-bb48-f3eb67045729 | -4.45193 | -47.92295 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 00613e48-ebe2-3ff8-9d8e-f3b817e27950 | -6.72109 | -45.57075 | 2026-10-02 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a52d79a5-c5a0-3fc6-bbad-4fb7180d9647 | -7.02725 | -44.50335 | 2026-10-02 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee5e39b4-474a-3e1e-a464-38aac2c3ae37 | -5.7482 | -45.1544 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd4dfc1e-caf6-3eca-9550-2ea8ea90f109 | -5.75959 | -45.15671 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a98db5da-d6ab-3c3b-b0ea-1a806fec25ed | -7.02785 | -44.49993 | 2026-10-02 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a17d8167-7a89-3b93-a553-80b0a9b6494a | -5.73274 | -43.28915 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28a52c0b-dca8-3189-ac59-ddfcdf99faf0 | -6.71383 | -38.99425 | 2026-10-02 03:53:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7594f69f-5e7a-33db-8ea3-435cd9e16dbd | -6.14339 | -47.27291 | 2026-10-02 03:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6ee658c1-22f7-33e5-bfd4-cd8357d7c7e8 | -7.58446 | -40.39096 | 2026-10-02 03:53:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11a36aef-bb52-3360-a968-975f539db310 | -6.31644 | -43.34395 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f831848-2243-38be-8214-593199f0e40e | -5.74166 | -43.28896 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b504f1b9-1ffd-34ab-8d84-051305ec2c70 | -5.74218 | -43.28606 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1f3063da-faca-3d85-b41b-91df05ea59cb | -4.45249 | -47.91705 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a13e1e70-27ed-3af6-b2a0-52b8df58c9a4 | -6.34241 | -43.36737 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1077259a-f53b-3a77-8080-dc10886312e1 | -6.09049 | -47.67252 | 2026-10-02 03:53:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fecfc77-373c-35c3-bc2b-5d789046e8d3 | -7.1994 | -46.54909 | 2026-10-02 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ac52ab6-9612-3e01-9e69-64bc09a5b1be | -7.53096 | -39.00232 | 2026-10-02 03:53:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f2816755-213a-383a-8795-8fb9187a2c5a | -7.20015 | -46.54782 | 2026-10-02 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7615d2b0-829a-39b4-834b-41a3d9dba092 | -6.33354 | -43.36481 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff30534c-6e6b-3a83-9746-0a0a31788ebd | -6.88944 | -43.69737 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb8d997-ae57-3afe-8e1e-2a015830cfcc | -5.54996 | -45.26433 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2559f427-1283-3c7e-8a37-07cd16a78fbc | -6.90684 | -43.68815 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 296ba690-1152-35d1-9cd3-014991386713 | -7.19246 | -46.55244 | 2026-10-02 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d22de48-9f73-3fa5-9eda-76b818a6d43f | -7.59131 | -40.80951 | 2026-10-02 03:53:00 | NPP-375D | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 016c0572-53e0-3d90-923b-38e6f6ade3e0 | -5.75096 | -45.13905 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0491980-d496-360c-81d4-dd2bc3917c8a | -6.34181 | -43.37702 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 173b846c-1f46-3d33-977a-00ed0bd5c7cc | -6.17165 | -44.58838 | 2026-10-02 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 062b83f5-94c9-3170-8cf7-b5f1b370d1fb | -6.2194 | -47.47448 | 2026-10-02 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33227625-5947-356d-96fd-42e8720d3632 | -5.76235 | -45.14128 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 17300229-931f-3f37-9e89-7c53be5f3fd5 | -6.33857 | -43.36571 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| decdda34-3692-3bce-800f-d860ca156d9c | -7.19931 | -46.55246 | 2026-10-02 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a4494e0-b27c-3634-9dfc-d771dc56926b | -6.91401 | -43.67721 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e9769ca-280e-315e-8e4b-2341f93f2eed | -6.34257 | -43.37258 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f4fdbb9-eeca-38c5-9a2f-1405f5b07dd9 | -5.76168 | -45.14503 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d5bc37e8-a5bf-3e61-a406-427ca1932bd0 | -6.08938 | -47.67861 | 2026-10-02 03:53:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0760258-f8c1-32d2-81c2-f2399d89ea8f | -6.90736 | -43.68515 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84a93580-cd03-3dd0-b585-fc675e495c86 | -6.12631 | -43.7271 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 188c979e-7567-3040-8f90-073132706814 | -5.76455 | -45.16198 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce49db9f-4f74-353b-aa09-991bc29bbeef | -6.14439 | -47.26743 | 2026-10-02 03:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3842c8d4-cb00-3043-a3cf-f32251a6741a | -6.91683 | -44.56193 | 2026-10-02 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63906974-4ce5-3118-9961-ff11f5b676bd | -6.32851 | -43.36393 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28bc8d79-4f53-30e3-8833-3a48f3d77c99 | -4.3649 | -47.7773 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee48923a-ac65-3e44-89c0-1f54e1e44d4a | -6.89964 | -43.69918 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d6885a-1924-325b-aa51-ccbad9a2b214 | -5.5538 | -37.32084 | 2026-10-02 03:53:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c38a7045-98dc-340f-8d8e-4555d4034f7f | -5.86952 | -43.59322 | 2026-10-02 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de318eb5-ca12-3000-8de0-44606d41af5e | -8.26526 | -39.07336 | 2026-10-02 03:53:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 592e5343-2aee-365c-a0b4-cae72192d9de | -6.90893 | -43.67624 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dd453f1-de32-3ef3-86ac-a41c7a77ee22 | -6.3436 | -43.3666 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8872a389-dd4b-3ff6-b317-a6e2224fcfd1 | -7.19324 | -46.55117 | 2026-10-02 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee5eab78-b0c1-330c-b693-43338f81c7b1 | -6.90789 | -43.68214 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 33cc141e-c008-33ea-aff0-3665b0e3a260 | -3.75027 | -40.55733 | 2026-10-02 03:53:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67c204db-99fb-306a-a956-c87d87bd6964 | -6.90474 | -43.70008 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f72d94f-e915-3135-8a80-48a4dbfcfaef | -6.2408 | -43.77663 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 133b091c-b198-3021-8876-d84fe9930dec | -5.73815 | -43.27934 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dde7e79-f7e7-3ff7-9543-f5da43f08d3a | -6.13202 | -43.72497 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41911041-4db4-3af2-a652-2c490e6126df | -6.92282 | -44.55964 | 2026-10-02 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51ca6041-e455-3e35-8c1e-b857dc3f9d6c | -6.15179 | -47.47347 | 2026-10-02 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a5a19d3-4371-333a-b0c7-572a7327427f | -6.13147 | -43.72813 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4550bcd3-263a-341d-9869-67bfa1016980 | -6.9135 | -43.68013 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 620ceccd-5b96-35ee-93f7-df2ecc276252 | -6.8889 | -43.70045 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 701c6dc9-354c-360f-955b-53db20a6a546 | -5.73765 | -43.28222 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8e2088eb-c876-3cc1-ba31-e2c7b12833de | -4.35805 | -47.77599 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dd73b6f4-847d-34d3-b578-00b45969a101 | -4.5112 | -38.2177 | 2026-10-02 03:53:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 551d6fa0-e0a1-38b5-8fa0-128dda08720e | -5.73323 | -43.28625 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca46dea9-4d4b-3e92-abab-0dbc13e0ff23 | -5.22094 | -46.02092 | 2026-10-02 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f17cdaaf-ca77-3cd7-a95e-5ea530c8b796 | -6.34134 | -43.37331 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6ed671f-8c9b-3f38-b5ea-2793a64fb80d | -5.7553 | -45.14771 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73f412fc-34f0-3284-8599-fe6d6603186a | -11.80264 | -43.58098 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b6b613d-2999-365e-bf03-d0c14a2a5764 | -11.7198 | -43.51051 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df01881c-217c-3398-8df8-1411a30eca89 | -11.77827 | -43.55684 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cadfce29-d22d-3a30-89f4-d63d78b4b3b0 | -9.82473 | -44.81658 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d45a3f17-4a1a-3093-8b84-a4d03712050f | -11.74978 | -43.58109 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 20345b69-bc2c-346e-b7f6-0286fdad6b20 | -11.72123 | -43.51233 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62461522-f8d1-3e73-b5b6-042ddab39a01 | -8.0143 | -47.43428 | 2026-10-02 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d261b0ae-273d-3a9f-bbac-91a518b0b93e | -7.87505 | -44.17278 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fbe17ea-7fbf-33dc-a9a9-bb12b09791ab | -11.68121 | -43.60049 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fd7c83c-7ed9-35ee-80ac-001abff0bde6 | -11.72226 | -43.42754 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9c92b60-283b-35c4-bbfc-6b31e7252534 | -14.55749 | -43.76456 | 2026-10-02 03:55:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b389455b-7dea-3368-b497-0548a65f7f99 | -11.74511 | -43.58036 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 52f78063-7fa3-3c53-8743-a46f3248aa33 | -11.41334 | -43.39769 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d890b95-9903-35f3-abb7-f0ae514ea3ff | -14.33227 | -44.74374 | 2026-10-02 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5dd40fe8-5fae-3c9a-ab6d-d09b972b3c09 | -11.69065 | -43.49633 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af66c016-540e-3042-8038-b926b055c557 | -11.14635 | -44.60686 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24dafd02-c5d9-3e9b-aa7e-f50ee9c00647 | -11.75614 | -43.57269 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 39a11c47-e50e-30b7-a550-e1bcf0c3d380 | -11.66723 | -43.59789 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 12551f2a-fe27-30b6-9f4b-5c3970a9c734 | -11.68035 | -43.60522 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa4dedc3-6c89-37bc-8c9e-67ca670d0261 | -14.03039 | -41.59693 | 2026-10-02 03:55:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 20bf3280-36c6-396d-83d6-41a5dff6cd7e | -11.76167 | -43.56877 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27693536-b9e2-352c-b667-d47d0a7bfeb0 | -8.38571 | -46.29638 | 2026-10-02 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8db37492-2231-36c0-8e0f-367f78bbfbfe | -9.503 | -45.33072 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1928e446-3325-3f1b-a766-26c17cd8ceba | -11.42963 | -43.4025 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9d6076a-64eb-334d-b67e-c9e6343e49da | -11.73258 | -43.44942 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bca7c13e-9589-3f90-b57b-125a72ad8917 | -11.41794 | -43.39861 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6e526a7-715c-308e-b890-2cc5fec2a3f8 | -11.7672 | -43.5648 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d08d5da-ed85-3bd5-8845-3b13370ae079 | -12.56567 | -43.06645 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 87bd8a22-d797-34c7-9aed-01619ca4f22b | -12.56848 | -43.07591 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 67998f9e-508b-3abd-89b0-e0b019605fb2 | -11.76849 | -43.58384 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 61cd4837-d988-3ea1-89f1-f07c28a68a34 | -13.33844 | -43.86476 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90a05751-2b40-353a-be91-440c4bb937a8 | -11.47417 | -43.44605 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
