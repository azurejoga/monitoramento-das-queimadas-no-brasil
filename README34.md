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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e2d3cb9-2ee4-37cd-8496-6e51fbe2b637 | -4.30276 | -44.49645 | 2024-10-31 04:49:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11019d04-d04c-3519-b985-454f33719279 | -6.13745 | -43.95735 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7032392-3e13-3bc3-b669-2a8db1b04aa8 | -6.13701 | -43.96048 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b6cd744d-06f6-387d-ab8f-95315e4069ed | -6.13657 | -43.96361 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8b1325c9-1eef-3f7a-8c07-bcc7e9b18663 | -6.13613 | -43.96675 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7622a506-4fe0-3528-bc48-507b74b8214e | -6.13569 | -43.96989 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 659b6cdf-13a2-305c-bbb4-249ee21d8324 | -6.13525 | -43.97297 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25437747-f4dc-3a88-883e-42c1665d23a8 | -6.13187 | -43.95961 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 11a90166-8e51-399e-8e89-829ad3a07e35 | -6.13144 | -43.96272 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f4127c3a-8b5a-3034-913d-9769887653b5 | -6.13099 | -43.9659 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ff76140-d857-3877-957c-f9f170524866 | -6.13055 | -43.9691 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0a64608-891e-33a9-a418-cc37b7f29d50 | -6.1301 | -43.97225 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e70487e6-be9d-39cd-b917-5a6ec2ce2caa | -6.12673 | -43.95878 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d573c485-2ed3-328e-be3d-7adffd0b875d | -6.1263 | -43.96191 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3b35abe-9c83-3f73-950a-0ca55a8fe10e | -6.12585 | -43.96509 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2d4630d-8957-3f94-8f19-4abba656b80a | -6.12541 | -43.96827 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 028f2fbd-1de5-391d-8419-1296b465d72a | -6.12497 | -43.97142 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dda0f4a8-6f7c-3bb2-bde5-12ffab0846ed | -6.12027 | -43.96746 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45e17d58-4328-3a9c-8521-5a6965f782a9 | -6.06646 | -43.62376 | 2024-10-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b3e037f-f1c3-3b83-9cee-cc72ec1957e7 | -6.06602 | -43.62693 | 2024-10-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca399beb-4cf9-38e9-a2c3-9d820270a8e0 | -6.06121 | -43.62292 | 2024-10-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88ea68e7-d47a-3070-84b9-67929f93c9c6 | -6.06076 | -43.62613 | 2024-10-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa3fd00c-8e79-3ce0-8434-780e62b41494 | -6.17584 | -44.01956 | 2024-10-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e298d8ae-f1e4-3f15-9e72-955914385cd3 | -5.81258 | -44.12767 | 2024-10-31 04:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba0d860e-7258-3ef5-aa96-9d6b26a4dc81 | -5.81216 | -44.13063 | 2024-10-31 04:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bd1fcb8-1d43-35bf-80a4-ed8b67505841 | -5.81174 | -44.13356 | 2024-10-31 04:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a4cf813-a705-31db-bbeb-c33ea236b289 | -6.68725 | -44.15816 | 2024-10-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 249bead0-bd47-3737-9137-7ba0431e6ba1 | -10.77723 | -45.04931 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9a5ad0e-a6a6-3a52-94cf-7f58664c83c6 | -10.77685 | -45.05237 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3226c4f-532e-3bae-950b-21286f712939 | -10.77646 | -45.05541 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75604c97-6ab0-3e63-ab33-441c8b085484 | -10.77404 | -45.05044 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1a3bc43-a1f0-3a8f-be96-ff5c3c085f95 | -10.77363 | -45.05347 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2539f0ae-dd3e-3854-b136-8f4934bcd946 | -10.77177 | -45.05141 | 2024-10-31 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e165be0-57f9-3b6c-a895-4f0fd411b155 | -11.05772 | -45.367 | 2024-10-31 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62f34ab2-4184-3842-b332-fccf165e5858 | -11.05734 | -45.37002 | 2024-10-31 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ec9c1d9-21d1-3a83-baa6-a3e9c3b2598e | -3.50975 | -45.78336 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3909257-6bfa-3c43-aa30-fe62a60ce4d3 | -5.05104 | -45.16169 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e6c4340-12a7-36a2-b76e-a62a2ddb4942 | -5.04636 | -45.16113 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 777e9230-2ed8-37a1-b3ff-52f2e35cffc4 | -5.04564 | -45.16599 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c3c11323-8e62-3742-82be-1299229f9dae | -5.0417 | -45.16044 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d5bab346-8772-3256-847c-b0d7f05ef21b | -5.04097 | -45.16534 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 303121c2-bd6e-3e3b-921e-d3fced052311 | -5.03632 | -45.1646 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ef7a3a-9be5-3a6c-98dd-2055a1e33905 | -3.89998 | -44.9319 | 2024-10-31 04:49:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c06392-7567-3eec-a7a8-a3b1ab72c098 | -5.0464 | -45.54077 | 2024-10-31 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34c1a180-8eab-3f1b-a155-c0d79d956e22 | -4.88089 | -45.90633 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83c3a328-afea-34b7-9acb-f17f3e5a2921 | -4.82812 | -45.83854 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 23101d33-03ae-35df-ae08-01d11f215f64 | -4.82748 | -45.84282 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a0e57e2-1582-308d-b453-c5d1d0083408 | -4.82371 | -45.83775 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e9bbfa9f-a363-3515-8512-0ab88d449028 | -4.82328 | -45.77959 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0e934fa-cff4-386d-b435-f4c0b9c34ab1 | -4.82306 | -45.84212 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 82f666d8-393c-3f75-b85a-e5b420bc86a2 | -4.82262 | -45.78406 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a20da4-5c77-3b61-bcb7-a530acfcc95d | -4.82241 | -45.8465 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 59e331b2-9077-376b-b367-7d17ac0a850f | -4.82177 | -45.85074 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 274a823c-7269-3b6f-8225-c15ff284977f | -4.81929 | -45.83701 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d9713836-aeca-342c-a977-900c620ba0f0 | -4.81865 | -45.84133 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 817b7976-2a91-3095-b461-4735a4ad5c68 | -4.818 | -45.84565 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3735bc91-2d26-3d36-9cda-470617dba337 | -4.81737 | -45.8499 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e88f22be-ee86-36e6-9d74-8dae50aceef1 | -4.81362 | -45.8447 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b312cf3b-e058-359c-bfaf-0e1b664fbc79 | -4.67002 | -45.68611 | 2024-10-31 04:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91a9e52-500f-33ec-89c4-48a68dc44fb0 | -4.57852 | -45.91406 | 2024-10-31 04:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c55613db-f913-3bb0-a614-2689e93f72a8 | -4.57789 | -45.91835 | 2024-10-31 04:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1314985-88cf-3f4d-9629-c28315233781 | -4.56205 | -45.96474 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729e2aca-4d5a-35bc-94b8-13a8a796cdb1 | -4.55614 | -45.55555 | 2024-10-31 04:49:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a3934ca-f176-3d82-bed1-33655310ef3b | -4.55551 | -45.55973 | 2024-10-31 04:49:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc18e5af-4693-3233-bb36-af2a8d1ebc2e | -4.55488 | -45.56392 | 2024-10-31 04:49:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3805772f-166b-3e55-a834-1758e32a72d1 | -4.5333 | -45.97788 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04dbfee9-fff9-3338-b226-3f9a409d8a38 | -4.52894 | -45.97713 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1661a307-b9f7-356c-9537-b38716e3ad33 | -4.4058 | -45.86605 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4481518-d62e-32b8-ab07-9b00d774dbf8 | -4.40138 | -45.86554 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf4aeb40-0f94-35f9-b7b0-e27c70faba6b | -4.38407 | -45.80076 | 2024-10-31 04:49:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581b02e3-e691-35e6-b045-a2af1387e708 | -4.37351 | -45.71929 | 2024-10-31 04:49:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54b4a5a4-47d8-311d-9fac-6549b91da199 | -4.36127 | -45.83289 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d99656e1-6925-3fde-88cd-8b3431eaf3d2 | -4.36066 | -45.83702 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd00255a-4be9-342f-98d6-c0d6ac58fee8 | -4.35683 | -45.83247 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2291d732-7843-32bb-bad5-ab7310ad98ac | -4.35621 | -45.83671 | 2024-10-31 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b70f0974-6293-3972-aee6-efaba2260981 | -5.32909 | -45.0082 | 2024-10-31 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fa588ee-a7e9-3f6d-babe-09c8ed10d987 | -5.28862 | -44.91423 | 2024-10-31 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bacee162-cea5-378e-b394-f1407ffd81c8 | -5.23078 | -44.91072 | 2024-10-31 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c554d1-fc2d-348c-88d2-42184c06675c | -5.22603 | -44.91 | 2024-10-31 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e082d768-62dc-34fc-9e45-259298b6eec8 | -6.19805 | -46.21069 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e3de0b-a53c-3093-85a1-be1541c47490 | -6.19742 | -46.21497 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c1ca75e-6c5a-3359-b65d-beae1e276092 | -6.1974 | -46.21204 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3ccb0cd-4eed-3d16-bb77-04ebb1c984e2 | -6.19679 | -46.21636 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb226596-a747-3e6d-b06a-5335a23fa174 | -6.193 | -46.21437 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24146b52-3bfb-3ba7-8d0a-4862715e0049 | -6.1016 | -45.97872 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07877de8-c960-3da0-9fb7-e5aa6b4e827a | -5.97533 | -45.36906 | 2024-10-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a3e310d-5627-3c6b-9133-18b23cae29d1 | -5.97462 | -45.37395 | 2024-10-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b68ca54b-1459-36c0-b12a-a695f93df6b7 | -5.97068 | -45.36826 | 2024-10-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aea87ba9-f72f-35c5-8038-d3423eb8ad7b | -5.96997 | -45.37316 | 2024-10-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da098219-f65f-317e-9f53-89054d1a1395 | -5.96533 | -45.37234 | 2024-10-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f5bdf03-93e0-35d3-a0fe-3d82c0d09da6 | -5.95234 | -46.47031 | 2024-10-31 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d077b5d3-19bc-3179-8792-c5fea6695424 | -5.28859 | -46.16043 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93ddf11-d920-3a3f-a094-36a345b0f4bd | -5.28424 | -46.15963 | 2024-10-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 455ab802-c5e4-3c0a-8020-d71131efccdb | -5.2449 | -45.84573 | 2024-10-31 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af7539bd-9115-3af3-843f-21ea1eefcc0a | -5.05802 | -45.80496 | 2024-10-31 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d265ad9-0477-3579-b990-4c500619eb72 | -7.61519 | -46.3758 | 2024-10-31 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31ec1893-2e13-3c82-9ad1-5fe17ce3bf99 | -7.61458 | -46.38017 | 2024-10-31 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8704b5ed-9432-3f7e-8be2-d04514a598d7 | -7.55532 | -45.53922 | 2024-10-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ddf3b6-8642-359e-a493-046fc7c1ab1e | -7.55131 | -45.53356 | 2024-10-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3583ad68-a556-3d22-aa8f-4f4351bd61f5 | -7.54729 | -45.52785 | 2024-10-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README35.md)
