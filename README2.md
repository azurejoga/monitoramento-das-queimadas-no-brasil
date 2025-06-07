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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 268706b8-df6d-315f-a302-215885a864ee | -7.73334 | -44.17884 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dbac3382-1e0b-3267-9094-ab0700873d47 | -6.95946 | -42.91925 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e0d3e5fd-1675-38d4-b36b-75af2cf6d3d1 | -7.02578 | -44.60287 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1a3c3877-ed67-354c-af65-2bf8b67a17cf | -7.20713 | -43.11526 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f6e5f8bb-51d1-3a76-b7f8-e4fd04c37ccd | -8.17151 | -46.49691 | 2025-06-07 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3f130d7b-2d6c-3c8b-933d-19c249692005 | -7.01804 | -44.61322 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 775664e4-860e-3f41-b592-8e3d26ef10af | -9.39698 | -48.43567 | 2025-06-07 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5ec0e877-5f04-32ae-9b01-bf97fa6e0b45 | -8.37968 | -41.80694 | 2025-06-07 00:20:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 331859ab-7baa-30da-b539-911ceb60f959 | -12.53355 | -45.42328 | 2025-06-07 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6eccd7b7-661e-3b36-807b-2b7044276983 | -12.95368 | -46.76851 | 2025-06-07 00:20:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 89c72ed3-f4bf-3b45-af20-dd227a62994d | -6.96705 | -42.90911 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d9115adb-c562-3ad7-a73e-d3984587130c | -7.7227 | -44.17742 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f85ab1bf-f889-3c33-bdf2-44442970b60d | -12.7765 | -48.71651 | 2025-06-07 00:20:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d141e404-1b32-3ff9-8413-d845e9bf34a6 | -8.20327 | -48.98603 | 2025-06-07 00:20:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 19b2190a-df37-3ab2-9cf2-9de9c4db4737 | -10.63294 | -49.44011 | 2025-06-07 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f8813b07-4342-3b84-8e4e-29def418ed21 | -10.64712 | -44.49178 | 2025-06-07 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fbb6439-0ae0-3b82-b47d-5fc5414e6b29 | -12.28708 | -50.11923 | 2025-06-07 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c887983e-e959-3bfd-957b-94ac6ed795c8 | -7.85947 | -47.90062 | 2025-06-07 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5098ccda-79ed-355c-a23d-0afe8ccfccbf | -7.86164 | -47.90892 | 2025-06-07 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a1b324e8-7743-3c40-977e-07a1f899424d | -6.59764 | -43.89236 | 2025-06-07 00:20:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b95e3e17-f686-38d1-801d-27ec656059b6 | -9.39918 | -48.45272 | 2025-06-07 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c3d6c1f9-1a84-3d7c-a7b9-5f72d3bb6460 | -6.21287 | -44.51437 | 2025-06-07 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48e0937e-a48c-39bb-99c5-0457b353be93 | -13.79355 | -44.08585 | 2025-06-07 00:20:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4719b260-82ad-3474-8fab-c764a4e4e733 | -5.45888 | -42.93211 | 2025-06-07 00:20:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 247a5cd7-9602-3b6c-8f84-e94eafbcb61c | -11.81264 | -44.2615 | 2025-06-07 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 88100f20-3515-32ba-bfd2-d524d6b1f5b2 | -11.77162 | -47.40307 | 2025-06-07 00:20:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 60ea9763-37bb-33ed-8b2b-a5286c5f80b2 | -8.87638 | -50.18775 | 2025-06-07 00:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 15a7dced-d318-3b0c-b4bd-ce00e85a48c7 | -12.28416 | -50.09348 | 2025-06-07 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 40e69432-9bdb-31d3-b5b9-d24da6b07dab | -7.01552 | -44.59483 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f7b8c24a-d9e5-3e1d-8461-8e2fba0fc327 | -5.78331 | -43.61332 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9adb6dd-1c13-3df2-bbd2-0c0a81c8e0fc | -5.64433 | -43.7286 | 2025-06-07 00:20:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 06d5b864-d01d-3ed9-9b75-c3652ea82389 | -7.73981 | -44.1596 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec7eb4a9-2f79-364a-9dcf-50340b7a8ee7 | -7.73089 | -44.16076 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ab46e605-66c6-399c-8d31-9e1b0416e7ae | -6.45057 | -45.7167 | 2025-06-07 00:20:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f29be89c-5eb9-3400-a32d-c38c65285e08 | -7.74103 | -44.16859 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 391e66e5-9a7e-3b72-92e2-5826d3cd49f8 | -7.72146 | -44.16837 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0035b6c8-3aa6-3223-97d6-f5f5e9ce96ce | -5.92652 | -45.52724 | 2025-06-07 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84b9fed3-9f1e-37a5-9032-44649bbd66e5 | -7.7138 | -44.17868 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c07dd692-2b2b-3b26-bd8b-7b9320fbae21 | -7.01678 | -44.60402 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e19eadfb-6579-3fd8-ba45-344e1c512e2a | -9.07182 | -47.15155 | 2025-06-07 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 855d31fc-85ba-328e-b909-625d861157e1 | -12.77893 | -48.73719 | 2025-06-07 00:20:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dfccfde5-05fd-3da3-b8ba-cf2405787e3d | -9.08253 | -47.15016 | 2025-06-07 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f252bb24-05c2-3d0b-98af-cc490c119df4 | -8.45628 | -46.4875 | 2025-06-07 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| fe1ce02f-9c83-3281-bec5-94525dd91f06 | -8.37724 | -41.85445 | 2025-06-07 00:20:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 38ffeaf4-0826-3fdf-9dc3-90e302f85efc | -13.07131 | -49.25411 | 2025-06-07 00:20:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e7635a92-8d23-3e43-a07f-e893f57b8f2b | -7.02451 | -44.59361 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 368c66f2-dc5e-319a-a0de-28dc628f123d | -6.19552 | -43.32657 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ba8325e-b61f-3428-97f5-6e794af204e0 | -8.89297 | -44.78746 | 2025-06-07 00:20:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 380ba53e-9a7c-3bae-9b36-c482cc5fb05b | -9.07011 | -47.13811 | 2025-06-07 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 17612c5b-9544-325b-9e4f-83af73ae3d04 | -5.64311 | -43.7198 | 2025-06-07 00:20:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| cbfbd90c-56d7-3c88-b858-673928308946 | -5.23876 | -36.20397 | 2025-06-07 00:20:00 | TERRA_M-M | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 44caef6b-dec5-3ab0-aaec-2beccfec828a | -7.71255 | -44.16963 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| ef5594d6-667f-3efb-94c6-1f2b6a3f6158 | -6.59885 | -43.90121 | 2025-06-07 00:20:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 50d43024-3642-30d9-bf1a-ca2f12ea4bc5 | -7.90329 | -50.36844 | 2025-06-07 00:20:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 74049049-fb26-3d89-8b3c-57f603394b81 | -6.54156 | -45.7081 | 2025-06-07 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5785c047-3a8d-3b72-a146-104de68eb2b9 | -7.72021 | -44.15932 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c46dec7b-5445-3ce2-9eac-b93799cc2f90 | -10.71203 | -48.78191 | 2025-06-07 00:20:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a16cd227-93b3-3b22-88d1-0ffe553e266c | -10.46584 | -47.94862 | 2025-06-07 00:20:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0ab6f8f7-f09d-39be-ab3c-177b2affbdc7 | -6.15146 | -45.97279 | 2025-06-07 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed319d44-9f36-3f92-854b-834f93ea7a2d | -8.58835 | -45.87008 | 2025-06-07 00:20:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c995536f-4f9b-3d9f-97cc-6ff4e5f860c1 | -7.21741 | -43.10746 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7e5ac8b8-3f0f-34ec-b141-85ff6cbde269 | -9.12922 | -46.88244 | 2025-06-07 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9922455f-8361-3215-957a-f59d3b3e17ec | -7.73211 | -44.16978 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2ebbd9e9-bc29-35b6-8524-ee4bfae977d1 | -6.45195 | -45.72677 | 2025-06-07 00:20:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ef99b49b-5c61-3c9a-bf25-072aaacdfe17 | -7.85978 | -47.89415 | 2025-06-07 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a6753dfe-b74d-3b6d-aa7b-131771cd9ec3 | -11.81393 | -44.27136 | 2025-06-07 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 97348060-0217-3a79-91db-3fc5b238f56a | -6.20555 | -43.33413 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 514c5c2d-1172-369c-9967-3815b8552659 | -12.2731 | -44.60411 | 2025-06-07 00:20:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b8d3a8b0-d445-3142-a523-f760567de754 | -12.32642 | -52.48082 | 2025-06-07 00:20:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c626d751-93f1-3e9e-a867-1db1151c49a6 | -9.50818 | -40.36954 | 2025-06-07 00:20:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cdc3a691-652f-31ed-b255-812cf34c20cc | -5.65069 | -43.70976 | 2025-06-07 00:20:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f98ae315-21a1-304d-8751-9bf3cdf39b46 | -9.08082 | -47.13676 | 2025-06-07 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8457205e-89ab-3362-9c67-ca6027730adc | -6.95822 | -42.91037 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 10a86e98-952c-3185-a5de-01e096418b69 | -7.21865 | -43.11629 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 003a9f3e-fb07-397f-b60d-704c0fff62a1 | -8.45784 | -46.49939 | 2025-06-07 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e021931-8ab3-316d-aa34-1f2d931940e5 | -3.05187 | -49.44228 | 2025-06-07 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 98f16d08-cc3e-3e40-95fc-53e9f3c37d2e | -6.96 | -42.9288 | 2025-06-07 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 2b0adc6f-4bab-3fcc-b918-409657750602 | -17.2639 | -42.6527 | 2025-06-07 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a4f41c3e-3742-3eb8-8ff5-fee05054de6c | -11.7826 | -47.402 | 2025-06-07 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 81a9156f-a16e-30df-9c2d-db4cc0bd86a6 | -5.6379 | -43.7175 | 2025-06-07 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d5370ba2-3dc7-3c66-8338-6206ffb062b8 | -11.3716 | -56.558 | 2025-06-07 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 72d1e18f-7ae7-3d2d-b404-6f0fa54765ea | -6.9602 | -42.9052 | 2025-06-07 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.4 |
| 66b93bea-110d-3015-aa95-a8dd21ed5153 | -11.2548 | -60.7957 | 2025-06-07 00:30:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 05e28343-333b-3031-87c9-10984ea0b34f | -7.7361 | -44.1823 | 2025-06-07 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2319a503-6ce9-315b-b5b7-79075f976835 | -7.7173 | -44.1842 | 2025-06-07 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3caedfde-6628-3e78-8889-28d0783193b5 | -7.7176 | -44.1611 | 2025-06-07 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 64bf0efc-3125-39cb-aa0d-15a2f77f7130 | -12.5238 | -58.3378 | 2025-06-07 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 75d64e52-6dc5-3566-9034-6034f6e7a381 | -5.6567 | -43.7161 | 2025-06-07 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b0b7e768-868c-3485-b0ef-18809f8f5f56 | -6.9414 | -42.907 | 2025-06-07 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| f814d4b9-38d3-3a9c-b815-4cefcfd5fe23 | -12.5236 | -58.3576 | 2025-06-07 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 0f5b078e-69e7-395e-a953-05b4717d1ad7 | -13.4733 | -56.8557 | 2025-06-07 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b3fc2252-beee-37fd-8057-335f05103c62 | -7.7364 | -44.1592 | 2025-06-07 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ed40fb83-df35-3d3e-b299-32949b49fde2 | -6.96 | -42.9288 | 2025-06-07 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 5d9ebc5e-5e7a-390a-90c7-dbe2cd863a1f | -12.5425 | -58.3561 | 2025-06-07 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 307d832c-81ab-3955-9562-9fa461a77954 | -6.9602 | -42.9052 | 2025-06-07 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.0 |
| 4dd61eb1-a342-350b-8d1f-14f2595fe78f | -12.5236 | -58.3576 | 2025-06-07 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 91a63ee2-4c8b-3a88-8064-33d905e2fbd7 | -7.0169 | -44.5954 | 2025-06-07 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b7c61a60-22a0-3bab-bc17-ac3bb9eb06f7 | -6.9414 | -42.907 | 2025-06-07 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 681e083a-035b-367d-8d7c-c25f86014295 | -17.2639 | -42.6527 | 2025-06-07 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 430b3776-b0e6-3dcc-858f-74eb24fc3406 | -11.7826 | -47.402 | 2025-06-07 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |


[Clique aqui para ver as próximas entradas](README3.md)
