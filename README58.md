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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab94974b-addd-3343-8c21-3730941474e8 | -5.75226 | -42.05775 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a6dfb49-87c6-3268-a55d-22b5dc6c9e2d | -4.34137 | -43.80141 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5adf8b56-2ebe-3148-b549-1cc0b1d0ad5f | -9.56029 | -40.33433 | 2026-10-08 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1e9c044a-a14e-3f2a-941e-3eb7922ce8f7 | -5.71546 | -41.76383 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 068dabc8-4e41-381d-aede-54f59cf7f97f | -7.46627 | -42.84889 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ce687de-5329-3cdb-bd38-7c9c77bb4c85 | -4.35222 | -43.80378 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8e71b219-b55d-389d-9e9a-f6d32621b952 | -5.23477 | -38.5503 | 2026-10-08 03:42:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9a8b66e6-6ec5-3ace-ae16-7ad8f77af0c4 | -6.82338 | -39.54423 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 132fc56b-39f5-3d87-aa08-8476337339d3 | -7.47138 | -42.85423 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dea81ddb-b4be-3577-a8cc-4389ed1ec86c | -5.991 | -40.93243 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c50a5c57-3833-35ad-a9bd-d2cf492acb88 | -16.00997 | -43.60082 | 2026-10-08 03:45:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cddc817a-e61e-3fee-9130-3625a2a90a83 | -16.89959 | -40.89481 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7e11d441-ebcf-3e77-b190-955b9368ea42 | -16.85925 | -40.58072 | 2026-10-08 03:45:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fcd3cabb-7876-3d60-b729-52392f7ee87b | -11.46186 | -43.38498 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df5cc23b-7001-3b77-b8f4-d992397e8cdd | -16.97645 | -41.22961 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 988b0cba-41b6-3b2f-82f5-78eaee9d94be | -11.30757 | -44.83337 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15660aea-f8d3-3358-a797-a16d58c5088f | -12.03656 | -43.44106 | 2026-10-08 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae7b4770-e9be-3115-a184-5bbed2cabc07 | -13.9065 | -43.99474 | 2026-10-08 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a136d308-f4c7-3a9c-8271-9d6e76288940 | -10.77483 | -46.58416 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 04dde00d-36fa-3d9f-9270-b12833862a84 | -13.15797 | -43.2802 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 5377f766-f557-3d57-a92f-cf0eaed5d4eb | -16.89178 | -40.88802 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f02d7505-a7c4-359e-a741-88add9d8fbdf | -15.62528 | -42.99099 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b7aa9ff-c079-3b1d-b6f9-9b6da352b74c | -11.7484 | -44.93618 | 2026-10-08 03:45:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aac6529e-7872-3c34-b2c0-3e51d5c14083 | -11.63796 | -43.70365 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3c2070c-19bf-30f9-a458-b06c8b4e5d68 | -11.63223 | -43.70225 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dd55a2e5-5005-3518-b0d8-4eab91591543 | -9.37127 | -45.93402 | 2026-10-08 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dd4c6ca-75ec-303e-918f-aae76877a976 | -11.2428 | -44.87939 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2baadfb0-07be-37ec-9b5a-5399b758f4fc | -16.12332 | -46.88616 | 2026-10-08 03:45:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93985eed-1898-3316-93bd-c610f3e74598 | -11.00511 | -45.42822 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f0407d5-22a7-33b6-8f89-89f250161213 | -9.37023 | -45.93972 | 2026-10-08 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1533c651-d73d-3c9a-b9f3-4ab07a5488b1 | -11.23511 | -46.25339 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7254e0cd-30d0-3896-a279-7a517990db62 | -11.62338 | -43.68589 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c59d485c-3f9f-3c77-9260-f45facdcf623 | -16.05143 | -40.64972 | 2026-10-08 03:45:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30dcb7c1-9577-3c06-a019-c1edcaa7a1e5 | -11.62698 | -43.69373 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88f75e1b-2175-3723-9d72-229d82dfbcea | -11.64581 | -43.68967 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 796e5760-c80c-3812-8ca3-716d3f60aaf3 | -11.63356 | -43.69086 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62123490-d0c8-3f94-8b85-7f344f675bd3 | -11.85996 | -40.19904 | 2026-10-08 03:45:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 552d9774-ef4b-3d0d-929a-13bd216fedd2 | -11.62785 | -43.6894 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 662071e8-b4dd-3c3d-9e46-e2d51d5ec51c | -17.11323 | -41.35557 | 2026-10-08 03:45:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| baf8a0ab-8494-3ad6-b284-31aea475ea51 | -16.84283 | -41.04804 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d700d05e-76fb-39a1-af53-df839b77141f | -11.38735 | -46.68369 | 2026-10-08 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f35861fb-350f-3afb-af9b-1325aecf8c21 | -11.73897 | -43.6425 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e236b7b6-eee4-335c-9290-d853943f9ac7 | -17.10962 | -41.3501 | 2026-10-08 03:45:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 086c69a5-6fef-3128-a174-669761fac90a | -15.42733 | -46.11083 | 2026-10-08 03:45:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c861afc4-aeab-3639-ab73-450bbc4c1214 | -17.10871 | -41.35476 | 2026-10-08 03:45:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9390e1ee-fd25-32aa-b98e-493220ff1422 | -14.92946 | -48.10474 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c4ab099-f4fe-3974-80c9-c971d9584e27 | -11.01042 | -45.43534 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59cab626-6280-31ad-8912-910b21286a9f | -15.55096 | -42.98069 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39464070-2f32-3505-a990-97961ebf3bd9 | -14.08094 | -43.76908 | 2026-10-08 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 392c9ed5-3dbb-3791-b435-56cf5dcef429 | -11.62611 | -43.69801 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b705ecc5-ebd3-3a77-b327-d166ac272951 | -11.45479 | -43.38537 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc2b1523-6fc8-333b-b36c-bda5a30fe129 | -16.13058 | -46.88776 | 2026-10-08 03:45:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 83c5a31b-611c-37c4-8a00-217e34282a9a | -15.55159 | -42.97751 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f6fa079-2782-327a-86ee-0b55eb68cf4c | -15.41953 | -43.70714 | 2026-10-08 03:45:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4f31309-b1d4-3438-9ca3-b8948a50d0d5 | -11.74392 | -43.64776 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fbb8e2b-6c3d-362e-ae3f-76c612db7586 | -16.83401 | -41.04602 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 02b72d8b-0da5-3d0a-8837-d01eff60190f | -12.15715 | -44.75702 | 2026-10-08 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f9c745-5abb-3050-b4e2-52f586a97808 | -15.421 | -43.70005 | 2026-10-08 03:45:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f040ba9-3c23-389b-a9c8-77cc732263db | -11.09446 | -44.00726 | 2026-10-08 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fc719ce-3317-3875-8aac-692e53a71821 | -9.91108 | -46.79379 | 2026-10-08 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6c7957c-0b23-386e-ad88-d69fa7edf787 | -13.19101 | -47.87399 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f46452c0-d0af-38b5-ab3f-0c1fa69706ef | -11.63752 | -43.7011 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ead3f1a9-d7bd-398a-8ff0-593b465eeffd | -9.8999 | -44.80234 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af0d2e1b-e360-3afc-bc78-83fe67f578e0 | -11.74471 | -43.64374 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f487cf5-82fd-3e1b-b10e-8c1611947237 | -16.90057 | -40.88961 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 349a721a-86bd-34ff-8ff1-69e90bfd1a36 | -12.81863 | -38.41585 | 2026-10-08 03:45:00 | NPP-375D | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c94bad58-6e22-3d02-81a4-8e282e4c9996 | -16.86352 | -40.5817 | 2026-10-08 03:45:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3c95fc78-dabf-37af-99c4-db58109eaee5 | -16.84372 | -41.04341 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| be4a6a5c-1776-3384-a174-bdb637028ac0 | -12.03727 | -43.4375 | 2026-10-08 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 044958df-f4ca-3b53-a41a-af048e6dc433 | -11.63837 | -43.69684 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c0a09bac-8737-3439-971a-2b1596be2bd6 | -11.62904 | -43.68767 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5518f31-4cee-382a-ab34-ea67a7dad5cc | -16.87676 | -40.60641 | 2026-10-08 03:45:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0349b0e2-a5cf-367c-b6ac-fb2b61e489c3 | -17.53839 | -41.69121 | 2026-10-08 03:45:00 | NPP-375D | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c7277fa1-2cbc-3d6b-8435-bc97ee5530ae | -14.91543 | -48.13394 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32914064-7327-3949-97b6-dc37823935f0 | -13.23071 | -43.39721 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f3326cd-c6c6-3e36-957d-3c1dd449884e | -11.78166 | -46.77221 | 2026-10-08 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ed7521d-584c-38f4-8168-f199736a2b76 | -16.90493 | -40.89058 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 09a6f00c-4a9b-3c9b-bf4e-b99fd2751337 | -10.77609 | -46.57808 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 922009b6-8baa-399e-aba5-e40588f37d88 | -11.30235 | -44.82716 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4ec7bfd-d0a0-3dae-8572-02d52ff82381 | -16.83485 | -41.04166 | 2026-10-08 03:45:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ac9d439b-edcf-3065-b85e-4b42aac6ec47 | -11.23524 | -45.24773 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bccf0341-10fd-373a-85b3-7d4ccc1a24c0 | -9.89886 | -44.8075 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5783cff9-7925-37f7-88c0-bf8b10295230 | -11.39243 | -46.69392 | 2026-10-08 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ce91fc3-d018-30f4-bcbd-ff0ce73066d5 | -16.12412 | -46.88635 | 2026-10-08 03:45:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| de832ae0-9a34-3b03-a0f8-93c45df63428 | -11.10126 | -44.00409 | 2026-10-08 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0be0d7ef-7fd4-33a5-82f5-f9ab7c276401 | -11.24083 | -46.25367 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b10a7d88-4d58-3c44-8ec5-777ee87e2bd0 | -10.96377 | -45.39936 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c9d4ad-c934-3003-b321-13afe5f7533d | -11.7178 | -43.65907 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2e9f84f-5f6f-3707-966c-3a9d9846c96d | -11.62736 | -43.69634 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 73b67092-506e-3937-bea8-951afe36ac9c | -15.42605 | -46.11662 | 2026-10-08 03:45:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db631cd7-267c-3a3b-b66f-4b3a94d9a246 | -11.30439 | -44.83089 | 2026-10-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed0962e6-a261-33f3-aa9f-6089899df6d7 | -11.77787 | -43.53374 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5154dc16-92fa-309f-84c0-45d05859500a | -11.71126 | -43.66195 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93c0deac-990d-3ccf-9c44-04ecac9b4c7b | -11.73818 | -43.64658 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 503e882f-37a2-3f1a-9fde-d06566429741 | -11.78275 | -46.77189 | 2026-10-08 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 096253d4-8a2e-3d37-b735-b4adc3bae229 | -9.90741 | -44.79793 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49410df5-5a05-3214-9f58-64744037031a | -11.24184 | -46.25498 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00927cd6-6e1a-3a57-a031-7d91631f7d68 | -11.23532 | -46.24603 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fcff88-18fe-38bd-b33d-449c5a7cb187 | -13.18936 | -47.8815 | 2026-10-08 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e775c24-ec1c-398d-86c8-447ed89ad8bb | -11.88284 | -40.96509 | 2026-10-08 03:45:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README59.md)
