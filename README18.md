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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d05ab41b-ff03-3dc3-ab7f-7bda6a312512 | -14.00615 | -44.04829 | 2026-08-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eefd9e78-cdd6-3c96-961c-6764249b0e35 | -12.21132 | -43.17112 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e8c1aac0-2bcb-3edf-8467-46568a4d9c6f | -12.78017 | -44.27607 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 724084eb-62be-3d38-b75d-813907231422 | -11.97843 | -45.90372 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e03722f-2405-33ec-aa9c-0a797cd01648 | -16.01586 | -42.98392 | 2026-08-25 03:32:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3dde61a-7a90-3d2b-8fd9-477843924f94 | -16.25306 | -41.77428 | 2026-08-25 03:32:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d7223e4-30de-39cb-badd-a4b28374f348 | -16.02064 | -42.98291 | 2026-08-25 03:32:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d7d13ed-795a-3169-8c82-116b161a6369 | -11.14334 | -44.48119 | 2026-08-25 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ae8cbc2b-169a-3a47-82d7-504c7e84ecce | -11.98269 | -45.91595 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e54cb027-962f-3517-8eb4-f824e0d645ce | -11.43224 | -44.53111 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 25c8a5f0-e0d5-3362-98be-d7c52550a597 | -12.73637 | -46.46838 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d9a8945-fe8e-3428-9674-1a49e4dd26fa | -12.781 | -44.27189 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 43c4a73f-323d-38d8-bfe1-629892c3d422 | -11.13733 | -44.47998 | 2026-08-25 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e2c11b47-8c66-3a72-9a3b-22cd81a56c3c | -10.37591 | -45.06569 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f80e3a50-26c6-3515-85dd-69a48f19e758 | -11.4004 | -45.16851 | 2026-08-25 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9722def7-56bf-3a47-886c-8fea6f4e550d | -10.36431 | -45.05809 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| c2d0c322-5392-34ae-b1ad-cf3ca6f54094 | -12.78267 | -44.26355 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24c71ffb-58d5-36fb-9e91-5765170cb13d | -11.97225 | -45.90187 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1aa4c5de-ec5e-30e1-9917-eafa9f46a556 | -12.2106 | -43.17481 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 153ceade-07a2-363e-a34f-7e710146f75f | -11.13642 | -44.48464 | 2026-08-25 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7f078725-926e-31c4-bf20-b054d39c42ed | -9.46133 | -40.32755 | 2026-08-25 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0c31b191-989f-383b-95ca-13451ea794bf | -12.20448 | -43.17725 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 83e249ee-9fa9-301e-8485-39c2a4b05cc5 | -11.39098 | -45.15092 | 2026-08-25 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9903ace4-ed8c-3178-8525-73eeabfc8271 | -12.45053 | -43.40597 | 2026-08-25 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5acf9a15-a10c-3f43-abd7-7beef7b1b430 | -15.6754 | -42.46937 | 2026-08-25 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8915d79d-3ac8-399a-a4fc-59c52675decf | -12.71714 | -43.20373 | 2026-08-25 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54291f24-7ef4-385a-8329-fe2570d68480 | -11.43554 | -44.54596 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9db5c597-ea15-3e28-ba9e-f838957ee6e9 | -12.73201 | -46.46635 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8c21168-87f2-3923-8cf9-0163babae017 | -10.36963 | -45.06433 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| e4dcb901-6fae-3d08-960f-4a022d480ffe | -12.71893 | -43.20419 | 2026-08-25 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25953939-1cba-3dcf-be60-3bee822d587b | -12.60559 | -44.6392 | 2026-08-25 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3fa0931-1361-3a40-9440-a9ee34c321b6 | -11.43913 | -44.52776 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e53af10d-3699-3b67-a06f-46c7732421b4 | -12.73499 | -46.47489 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fc7ec82-5ea6-3834-8fe2-24779d6b8f19 | -11.80961 | -46.66989 | 2026-08-25 03:32:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67e3a6a0-ff29-394e-b001-c7700d0b0ee9 | -9.69268 | -46.05742 | 2026-08-25 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36c3de64-1183-31c4-ba84-1a64a77cf160 | -11.99349 | -45.92908 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43b92ad2-0bf8-3e55-a62b-a89b66781a57 | -11.98287 | -45.91545 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fdfe35b-f7b7-327e-85a5-7ee19dc73201 | -11.14423 | -44.47661 | 2026-08-25 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e02fb372-dbde-3559-8c3d-b590f5dd734b | -11.88877 | -43.82951 | 2026-08-25 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 541c4557-f3fe-3066-a303-501db2a84183 | -15.68226 | -42.47258 | 2026-08-25 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 674a82c4-63d4-34ba-98c4-15ae10f8081b | -13.09054 | -43.36914 | 2026-08-25 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 502651e8-1094-395d-a72d-ad73d765449b | -12.60647 | -44.63479 | 2026-08-25 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c122f270-42bb-3bf7-8fc3-041c7463c763 | -11.43374 | -44.5551 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c957aab-00db-3817-b86d-bd0857a76fb0 | -12.20246 | -43.18754 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2f185ee-5239-3433-a1cd-5d0117998979 | -11.88385 | -43.8244 | 2026-08-25 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2954cfa5-ee57-37ee-98cc-14b4d08170c2 | -9.69721 | -46.04456 | 2026-08-25 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89e0ec35-eb86-3b2f-826c-0c9863148d23 | -12.12915 | -43.3877 | 2026-08-25 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7e54228-f0c6-36b4-aad4-1d5d6b20284a | -11.98695 | -45.92822 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7da41b3-98ad-31e9-a0fd-fbb34be30985 | -11.97755 | -45.90868 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0604ded8-7922-3719-872c-f5d889067c6a | -13.99982 | -44.05096 | 2026-08-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| feb7aaee-3e52-3db2-8cfb-9b5be898959a | -9.70272 | -46.05204 | 2026-08-25 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 670f4590-5ad5-3bcc-8e30-3fe5c8480cd5 | -12.74151 | -46.47654 | 2026-08-25 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3be8d748-4882-30ad-9d04-e583a0bbab87 | -12.77691 | -44.26239 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 05842879-22c5-32da-8ad1-e5984fb9f650 | -11.88306 | -43.82842 | 2026-08-25 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6dc162ca-1e62-3453-98d7-7b85d5e5f4d2 | -12.19711 | -43.186 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be328988-590b-38eb-ae9f-fd14a619446e | -16.623 | -43.41766 | 2026-08-25 03:34:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4a0d409-9c66-3ec4-956b-02dad5160c5f | -21.14092 | -50.23576 | 2026-08-25 03:34:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 15093a24-7019-39d1-8feb-668ff17d6935 | -19.27798 | -40.32808 | 2026-08-25 03:34:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11cf47eb-1497-30fa-87cc-e72f45f4f5ba | -20.94305 | -44.7767 | 2026-08-25 03:34:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1657478-aa53-3d93-91f9-ce4a42c9903b | -23.16853 | -47.09842 | 2026-08-25 03:34:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7ad9cef2-093e-3548-b7e7-93d81d5b44c5 | -16.43808 | -43.46621 | 2026-08-25 03:34:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b874a7fe-6945-389f-b943-ef2c59008c8b | -20.94375 | -44.77342 | 2026-08-25 03:34:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43c25fbc-1ce3-35ce-a6de-554d45ac25b0 | -22.15833 | -46.65401 | 2026-08-25 03:34:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9759c8d2-ba5f-3ece-8d35-930cfd5bb909 | -16.62239 | -43.42067 | 2026-08-25 03:34:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 112e3690-4dfb-3555-8c84-143c32ece3b9 | -16.13968 | -48.90087 | 2026-08-25 03:34:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94719b30-13e1-3858-a097-ade0535fe4b3 | -21.13911 | -50.24307 | 2026-08-25 03:34:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d93d6897-6b35-36c0-9661-41e567e60714 | -23.16744 | -47.10312 | 2026-08-25 03:34:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 48fbf701-be7d-3d3a-b50f-271177517208 | -21.13839 | -50.23916 | 2026-08-25 03:34:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9abe9303-c87d-3332-a466-2139534fb97b | -21.13404 | -50.23386 | 2026-08-25 03:34:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 85e62ed8-7f2b-353a-a27a-c3796abcf141 | -21.51243 | -45.75846 | 2026-08-25 03:34:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 41789fdd-d81a-36c0-9118-ccf84850f446 | -16.4432 | -43.46725 | 2026-08-25 03:34:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69c2644c-dd78-3ee9-87a0-9270edd28220 | -16.3799 | -42.97725 | 2026-08-25 03:34:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe3ea0ca-3940-3069-b99c-cc4b690bcc70 | -22.45232 | -47.41022 | 2026-08-25 03:34:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 634eae6e-d6be-312f-8ff4-3334220dd7b6 | -21.1315 | -50.23729 | 2026-08-25 03:34:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e983454a-dd8f-377a-9381-a34a5ac576bb | -21.50715 | -45.75688 | 2026-08-25 03:34:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6021766-9095-3e3f-96b2-119a4b777652 | -6.9872 | -59.2582 | 2026-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 36fa0ad2-3dc6-338e-b9b8-2f12edffd813 | -7.2901 | -45.3683 | 2026-08-25 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3d951bd6-e44c-3ed8-a291-9882d88b2323 | -7.2903 | -45.3456 | 2026-08-25 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b9a34c28-3d8b-3913-8618-1572b033fddc | -6.6226 | -58.4995 | 2026-08-25 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de48f663-9d8d-3054-bee6-d65f3823a9ab | -7.0058 | -59.2382 | 2026-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 3bc222b2-70fa-3e9f-aaa0-9d79c6385160 | -6.9873 | -59.2389 | 2026-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 56173b5d-413a-3b0f-a7ad-3164350fc08a | -11.1252 | -44.4892 | 2026-08-25 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4a09aa66-af2d-3915-96f8-ad71400b02ca | -11.1447 | -44.4632 | 2026-08-25 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 7ac6e0e0-d7e1-333a-acf8-607437b60713 | -11.1443 | -44.4865 | 2026-08-25 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f6f9f3c2-66d3-39c2-84ed-df5f618dbb24 | -7.0057 | -59.2575 | 2026-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 9eb15202-8720-32e3-b420-22710517af0a | -3.5407 | -48.1673 | 2026-08-25 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 0fd93074-0332-3815-8764-47c610fc7e0f | -3.5222 | -48.168 | 2026-08-25 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a29cff79-708a-3907-9165-a9c77c39005b | -6.641 | -58.4987 | 2026-08-25 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 6f903b41-9046-38b0-b15b-51fb370af11b | -10.3727 | -45.0537 | 2026-08-25 03:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a1fb66ec-1c74-367e-a5d7-eedfd764bd1f | -11.1256 | -44.4659 | 2026-08-25 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| eecc1673-2047-3e45-b079-046bff10183b | -3.5221 | -48.1896 | 2026-08-25 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 295a3a8c-b8ca-36df-8a72-699cb249ea09 | -7.2713 | -45.37 | 2026-08-25 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 151c6dc5-31cf-329f-b5fa-639a349eb3f5 | -3.5406 | -48.1889 | 2026-08-25 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| f3b09a8d-6cf6-3fd6-a654-0fa09f682195 | -3.5221 | -48.1896 | 2026-08-25 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 5eb4b704-89b2-3c08-886e-5277b42f30d9 | -7.0058 | -59.2382 | 2026-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 0b3bcae3-b352-3611-8069-2df7759f6052 | -6.641 | -58.4987 | 2026-08-25 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 40c2cf2a-2eb2-3fd8-aa99-15ffb4d512e6 | -7.2903 | -45.3456 | 2026-08-25 03:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 432a451c-0deb-30a8-bc52-d7f7d3232716 | -11.1256 | -44.4659 | 2026-08-25 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 50dc342a-8435-3caa-993b-1291c82fbb7f | -10.3727 | -45.0537 | 2026-08-25 03:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c4074719-2414-3127-bd34-a3d010b6a00f | -6.9873 | -59.2389 | 2026-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |


[Clique aqui para ver as próximas entradas](README19.md)
