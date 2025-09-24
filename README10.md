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
| 22d89ac7-91e0-3b92-8fc7-7d6208270b7a | -10.57857 | -44.07953 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdb26878-1eba-30fa-9132-4dd0e03ce871 | -13.27151 | -44.56737 | 2025-09-24 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 823d7c64-af21-37c9-995d-d2af2d398c9a | -10.58361 | -44.0717 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7894f3d-783d-3374-a79c-f0adf727d851 | -16.51614 | -43.54754 | 2025-09-24 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4aebfff4-afc0-3e4f-9c65-482f591899a2 | -11.92645 | -38.33245 | 2025-09-24 04:02:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4355b6a9-482b-334c-b945-c95c678197ac | -12.66775 | -44.35433 | 2025-09-24 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed836650-b365-3a9b-8d2a-c9ed17960a27 | -9.5758 | -47.58168 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ffb90fb-bbcc-3942-bad4-3bae5ef6fe91 | -11.51924 | -43.6617 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64b56f93-c345-3d32-9a0d-8d882527dd36 | -10.45031 | -40.56865 | 2025-09-24 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dab580d-8b61-341e-953c-a11eca784257 | -11.63792 | -44.35866 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 190d1d35-bf34-3bf4-a1ac-175fcaabda27 | -11.70179 | -44.35941 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac0cc74b-c2f8-3c77-9d7e-7b3932abef2b | -11.42414 | -44.93073 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29eda8b9-16e9-3237-8040-f3d5f7d8e848 | -11.81305 | -45.31316 | 2025-09-24 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9161ba7a-6dae-3f28-9db1-430129473f09 | -11.41482 | -44.96258 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fff4772-c684-3629-b8b2-1208ad08ff6d | -16.17949 | -43.65038 | 2025-09-24 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5b6c2c0-3877-33a6-8730-b612c50fff8a | -12.18001 | -47.75346 | 2025-09-24 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bcdd59b4-1fba-33cf-8b0f-e03141d6c44b | -10.58142 | -44.06264 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4650d56d-6dba-3ef1-88c5-1605bae8cefe | -13.61327 | -43.9818 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bef00db1-5db3-3bec-88d0-e4af2a21ef6d | -11.01046 | -45.89861 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30d19f53-ae96-349d-b08d-510d2f1ea9ec | -10.6262 | -49.06137 | 2025-09-24 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25cc69be-f54c-3ea4-aeb0-683f649ff8ee | -14.291 | -41.83976 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8227a14-0405-3213-92e2-cb95158fe8d3 | -16.5195 | -43.54814 | 2025-09-24 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cc224d7-1ddd-3000-a264-cb33742efb44 | -11.01721 | -44.49903 | 2025-09-24 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e0c572d-a91b-3a44-9cb0-7451975005f8 | -11.42042 | -44.92989 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79a46865-311d-31c9-ac8b-528da202a0c3 | -11.00988 | -44.50423 | 2025-09-24 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bdb20747-2049-3fe7-ae1c-adc3a18465e9 | -14.29044 | -41.84331 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24bfe234-caf1-3f49-ad4c-62485c3565bd | -11.51573 | -43.66109 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2a0212e-13cf-3a80-a7ec-b816e3b253b6 | -9.55714 | -47.55409 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b5faeb9-02ee-3bbe-928c-305ad96f237a | -9.58741 | -47.56922 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0b9a85a-4b0f-3f46-829d-087627438ce2 | -11.69452 | -44.38007 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d68a30-929f-3f59-926e-84420179c098 | -10.88754 | -44.02877 | 2025-09-24 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f14c2602-452f-3b48-be67-94a375740b40 | -9.45309 | -48.90499 | 2025-09-24 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97d36fc5-0679-38ff-91bf-1997c48cb0d2 | -11.01169 | -45.8916 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a056121-feb9-33c1-8ab4-11fedfae5ff0 | -12.0725 | -44.77908 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4864ca8b-875d-3606-b0cb-c654c28e0c0b | -13.8167 | -43.22577 | 2025-09-24 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12b70775-45ec-3bf9-9ec5-ae22974b9407 | -11.64226 | -44.35504 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94198f98-fe46-3614-a81e-729e5138febe | -16.51889 | -43.55185 | 2025-09-24 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95276865-8f6e-3e55-9a9a-a9b627001cf1 | -14.29375 | -41.84386 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 2e2232e4-dd66-35cd-a60b-28f52fa21f39 | -15.67342 | -41.31262 | 2025-09-24 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7cdbec71-115d-3c0f-9c7c-84b0a7846557 | -11.46712 | -40.99072 | 2025-09-24 04:02:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e99120a-fffe-3a0c-b35d-36ea994e4082 | -10.84931 | -45.41756 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46328184-8fbc-3f9c-86a6-a2c02ca455ab | -15.35105 | -41.85854 | 2025-09-24 04:02:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 53f08a87-2655-3ec6-b847-7a7742f988f6 | -13.28247 | -39.02478 | 2025-09-24 04:02:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e27d40de-e080-3fae-8e3c-feb7d97d6274 | -12.1792 | -47.75782 | 2025-09-24 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79a41792-0f3e-35ab-ac63-f11d0f08d3e1 | -12.39737 | -45.01023 | 2025-09-24 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da3376ed-c462-398f-bf63-4ce4cf1089e9 | -11.68215 | -44.38403 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d63211ee-0a17-302f-a409-72ae38ff3e06 | -13.8127 | -43.22891 | 2025-09-24 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c66b6a60-03dd-3982-b28f-49924d7f62ef | -12.08435 | -44.7763 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be12cce-8b8d-3fe0-836e-f0dfb5a4a6b8 | -10.85319 | -45.41823 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09d0c32b-3bd1-3ae2-adba-ca9153c47f7c | -13.62975 | -43.86333 | 2025-09-24 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51fe8c70-fefa-3699-aaa9-1ff44fa6f9ad | -13.38817 | -39.95226 | 2025-09-24 04:02:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48b95213-08b3-323b-8747-58c5a776d8b8 | -11.82374 | -43.16082 | 2025-09-24 04:02:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b665bce-455f-3707-9e69-00433a2c3d86 | -11.66622 | -44.39002 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fee4ba8a-af93-33ba-8dd2-d6b00b54021d | -14.29819 | -41.83732 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| c50e0556-4ba8-31a9-aa33-a628461878e6 | -14.29157 | -41.83621 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10bac21b-bed3-3af5-aa96-b93d40f2554a | -14.29431 | -41.84032 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 1e4bb645-b5ac-300d-b567-280db362a5a4 | -11.69817 | -44.35876 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 788596da-7608-342c-b449-411b922dddf7 | -10.83273 | -44.8213 | 2025-09-24 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0346fd05-21a5-3ae1-bfaa-01a5b57273b6 | -11.77539 | -44.87512 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e51a851e-c29c-3471-9464-4d5168358c7d | -10.5829 | -44.07593 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58425786-4219-3644-9e3f-7004a3fc05e0 | -9.11157 | -49.62898 | 2025-09-24 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a2fe019-7a50-3cf3-b28e-8f43b44fe3e3 | -12.39526 | -43.82215 | 2025-09-24 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f94bb74f-e694-37da-ae8b-d015efb27339 | -12.18062 | -47.75569 | 2025-09-24 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 80efcd64-fae9-3f09-8587-92d7652d6eef | -13.61675 | -43.98242 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b141d2f-ed40-3fb3-b597-8df9437b68a6 | -11.4081 | -44.95673 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657807a2-2c42-3a76-adc0-a62dff980c40 | -10.2467 | -40.54744 | 2025-09-24 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e6ae3136-f765-3b43-8d40-232402e9972d | -11.52208 | -43.66631 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17713eac-bab8-3d0b-8aec-86267f3a298d | -10.5858 | -44.0808 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e62d54c-c5e0-3eb1-990b-e6aa0d6be90f | -14.81511 | -42.32552 | 2025-09-24 04:02:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38c7801c-7e1b-39f6-bec6-85931bcbd8c9 | -15.67287 | -41.31622 | 2025-09-24 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5d503623-346e-3327-a6c5-1b4bd4c489a0 | -16.31199 | -42.98872 | 2025-09-24 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6623000-36e9-3d5f-8221-bdaf8de20af3 | -9.73231 | -48.65208 | 2025-09-24 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 499ac01e-f905-3455-a0d8-4c44afd4c66c | -12.08361 | -44.7806 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36bc9144-daf5-321a-9f68-4adce80a245a | -10.57785 | -44.08377 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 059d8ae0-864b-37a6-9fe3-05571a517cde | -9.45259 | -48.90776 | 2025-09-24 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2096baf-92ca-32ee-bc00-9b8f2c7d3089 | -14.29762 | -41.84087 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 54d2deaa-f78a-3e6e-b204-c472ef2b838a | -14.74793 | -41.1554 | 2025-09-24 04:02:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a9a40f04-99e8-3e45-91e3-e1ae507eb781 | -10.57929 | -44.0753 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eccd3c30-6a6b-3253-9de4-5508e87faffb | -11.08248 | -43.14499 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ac1da9a-64f2-3f64-b490-cee2696c1418 | -10.83352 | -44.81657 | 2025-09-24 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a52554d-69bb-3ad8-b041-9fcdec28360a | -10.58219 | -44.08017 | 2025-09-24 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e68043-84cc-3752-a4b5-4a7690134329 | -11.00709 | -45.89438 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 487aa77b-7ba9-3082-b3cc-5676b93f8a13 | -10.58651 | -44.07656 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bccd472-db73-308f-a577-319783739a4d | -11.46663 | -40.99421 | 2025-09-24 04:02:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04673617-e87f-3d60-b5db-096023f4c9ee | -11.42622 | -44.94107 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 97e747d6-7255-38dd-ab9d-f3b550b4e681 | -12.05818 | -44.81797 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b71b55fa-56b7-3303-9a63-426d18706d37 | -9.56254 | -47.55017 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e00291f6-dd31-37da-a589-e93e7d463a3c | -11.9018 | -41.67805 | 2025-09-24 04:02:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 492cd086-2916-3267-a67d-414544dd9947 | -12.1814 | -47.75134 | 2025-09-24 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a63d3d2c-5ff9-3ec6-b45c-40d3bd5fb1c9 | -11.52425 | -43.67496 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02a9b28e-8060-340c-a1cf-a784beb88f25 | -12.0688 | -44.77854 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3557d772-39bc-35d0-a755-ff717dd768c0 | -9.1088 | -48.90034 | 2025-09-24 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c27f8af6-9226-37f4-a7a9-b021ebcf8332 | -14.0542 | -43.12473 | 2025-09-24 04:02:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 115338c9-0762-34f5-b083-3abaf11066ea | -11.67852 | -44.38339 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d53509d4-4a04-3c77-aae3-027e6adb4922 | -12.06423 | -44.80497 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 068d8c97-f4a2-3295-941c-16332d2bbaea | -12.88935 | -44.65625 | 2025-09-24 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91fa142a-bd97-3709-ad35-fe9b5270d8a2 | -11.62922 | -44.32208 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8b8a5e1-1526-360a-8cfc-5c05ff0ab4ee | -13.81331 | -43.22518 | 2025-09-24 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e677ede-d737-3c0d-8d08-60dd76748126 | -13.44922 | -42.9466 | 2025-09-24 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4901cc0c-0c69-3888-b542-29dcfa3740d1 | -10.58071 | -44.06685 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
