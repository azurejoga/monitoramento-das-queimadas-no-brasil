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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e5c312e-ba70-3886-b66d-d74063d674f8 | -12.03104 | -46.02931 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d41cf0-39e9-369f-a284-e32ceff09d99 | -12.03293 | -46.03959 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e2eaad6c-75b2-3755-9cdf-0ad67e282b5e | -12.66438 | -48.40918 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec0023be-5a4a-360e-8b8c-a7b1b05449cd | -12.72711 | -48.37866 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb344266-76ea-3007-8886-5ffba57bcd61 | -5.34216 | -45.16281 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb5db459-7827-3577-81bf-d6a238ff20a8 | -5.34759 | -45.1689 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7cde43a4-335c-3c0c-baf0-ebe0e8b25111 | -5.66201 | -46.95647 | 2026-08-26 03:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e226a22-8d19-3f91-857c-bb7535d201c8 | -11.27986 | -47.07327 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f23578dd-763d-39cc-9be1-87cf9d40cd8e | -4.8083 | -45.76759 | 2026-08-26 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aeba8280-4655-3cb9-b7fc-5c64c9223a40 | -6.32071 | -44.84358 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b449f9ca-d543-3227-963a-0f4f70c96499 | -14.78966 | -48.80696 | 2026-08-26 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f6886dc-ca02-349a-856c-e17cf92ef9d7 | -11.79435 | -47.64214 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a1bdc46-0ab5-39bc-ba56-0a16926fcb3a | -4.84646 | -44.29354 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5532cba-c512-315d-86b0-310551961935 | -11.01327 | -45.07278 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba311cfc-c535-3e57-a344-14e29e347ba5 | -12.03518 | -46.03933 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 57460cf5-faba-37b9-b330-9cd44a53abe4 | -18.76098 | -41.29844 | 2026-08-26 03:49:00 | NPP-375D | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd85150d-ca63-3794-ba13-322e72623eeb | -5.33804 | -45.16274 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31185433-70a2-37ee-9c68-84c30acc4558 | -12.03379 | -46.03519 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 103595d8-14ae-3d1b-bb27-cf9055ee0b25 | -11.25021 | -47.05498 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c882a56e-5068-309c-b1bc-cabaf482b547 | -12.76307 | -44.25929 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc4ae5db-c43b-39c9-ab60-514f9d4c6992 | -18.94684 | -41.01268 | 2026-08-26 03:49:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ded3e536-e353-31f8-a6ff-142890555fd2 | -6.95142 | -42.68501 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddd1c246-5af2-3712-a85e-98e9821630db | -11.82231 | -47.66286 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4606a9a-6722-3a74-a9fa-f32ead04e7f3 | -6.88765 | -43.74631 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d9bfc4d-98d5-3632-897b-0f39b3067620 | -17.77559 | -47.0924 | 2026-08-26 03:49:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cde6f63-fd32-3e46-baaf-99bdd5a73ab6 | -11.42745 | -44.53522 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e044ef69-188c-3a82-a3fc-fa9cdd7073b1 | -5.65502 | -46.95533 | 2026-08-26 03:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c63a8c90-1510-315b-b664-edc8a58602e2 | -5.51557 | -44.11723 | 2026-08-26 03:49:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e00755cd-418a-3163-8c6e-d0da9446a2a3 | -6.1316 | -44.07377 | 2026-08-26 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07b2eff8-46e3-3da6-9398-a21a291d89f0 | -12.03429 | -46.04372 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3f6b23dc-980e-3aaf-8caf-33af44dfd556 | -5.74171 | -43.27711 | 2026-08-26 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72f015ad-07b8-34f1-b6b8-288f7a8d7f88 | -12.0212 | -46.00504 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c4196637-baa1-3cb3-976e-03442d0ac84e | -11.8192 | -47.65447 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f5424ee-dbaa-3f5c-9354-bca5d3e5cdd6 | -13.60579 | -49.0134 | 2026-08-26 03:49:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36e3e2d6-17a5-32a2-b6e7-1a61a9913549 | -6.87078 | -43.7434 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fa2022a-150a-3013-b08a-e681d6b2a68b | -11.01638 | -45.06484 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2bd2e7d-ac18-3841-b06c-47f27ebe9129 | -12.76893 | -44.25711 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e63682fb-1a2d-3fc9-8258-0a8a9132837f | -11.4213 | -44.53774 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af8daf88-0a52-3049-897b-3e101fd9eb21 | -6.9182 | -41.12242 | 2026-08-26 03:49:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 855561fd-1673-3d74-9887-560de85d8574 | -12.26237 | -43.11172 | 2026-08-26 03:49:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eea18091-5805-3009-8dc3-718ce1a76e88 | -12.02453 | -46.01948 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fac669cc-884b-3f26-95d8-6076c27f5a37 | -15.6951 | -43.79226 | 2026-08-26 03:49:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21334cf0-c3ee-3392-9b32-89248af7ea11 | -15.06127 | -45.32491 | 2026-08-26 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3fb7ea-2a05-3cd1-9c65-b9e79def4438 | -12.6844 | -48.42209 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3879b9ee-b9f9-3e83-8cf8-bc50fdfe8a5b | -12.75848 | -44.25494 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c95af1a-87e1-32ff-8c19-576ddb1a00c0 | -5.34519 | -45.15913 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f041fa84-6904-33cc-9472-c8cb8582eb23 | -5.51832 | -44.11589 | 2026-08-26 03:49:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9bfc4a4-11e9-3251-adfa-352bc09defad | -5.34128 | -45.16783 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dbf3d17d-b8eb-3d77-88cf-0016b47f7467 | -18.94436 | -41.01536 | 2026-08-26 03:49:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ce4ae429-ee1a-3d1c-9b7f-098ff9954723 | -12.72758 | -48.38534 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad3aa09b-3d3a-38c7-a164-3c6200e03902 | -12.66151 | -48.42274 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 76fd4038-2177-347b-bdef-90a6bf47f004 | -13.61274 | -49.01451 | 2026-08-26 03:49:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e826373b-d283-3eac-ab8c-4678a33cdd46 | -4.84668 | -44.29936 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37f8a3ae-c8d9-33cc-badb-0ee0757140c5 | -14.62106 | -42.52729 | 2026-08-26 03:49:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22f597f0-1e22-32a2-ab31-5997a56b841c | -12.02034 | -46.00941 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4e765e0a-1267-3840-b2bb-11faf75037d3 | -12.68044 | -48.39991 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f91e9985-4311-349a-b73d-e00258ea406e | -11.37317 | -45.16208 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ece14a97-2f5a-3898-879a-83e83a5750f9 | -18.21466 | -41.57289 | 2026-08-26 03:49:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03c5c0ba-43cb-3d9c-9ddc-a2048b6f505f | -12.02796 | -46.00196 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6e83506-fe72-3f23-84ad-4f5550919389 | -5.73617 | -43.27602 | 2026-08-26 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0a662bf-a62b-32d6-b300-45848b18c142 | -7.08932 | -42.18217 | 2026-08-26 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 257ced3b-13c8-39e4-8d65-dc80e2945247 | -11.48866 | -45.09367 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8b6b9ac-852d-3925-8807-12bb52ee54fd | -6.13242 | -44.06917 | 2026-08-26 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1955e827-5832-340e-a910-849310623de2 | -12.0269 | -46.01929 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8394792f-adbf-397a-b2b7-60621e747302 | -12.02837 | -46.04244 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8eb35cae-f44e-3466-9ff1-4fd079b6c7fe | -5.9211 | -43.64386 | 2026-08-26 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dc99c79-0f64-3fb2-bdb9-ceabe04f67a5 | -12.68654 | -48.41221 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b83a62c1-9362-3294-a095-02a455721d59 | -12.70074 | -45.83022 | 2026-08-26 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e46c96f8-7a25-3213-968f-bc19498307e4 | -11.41993 | -44.54491 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5827c072-b459-32b7-b1ca-3651d3fbf485 | -6.26962 | -36.03752 | 2026-08-26 03:49:00 | NPP-375D | SANTA CRUZ | RIO GRANDE DO NORTE | Brasil | 2411205 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab3366de-9773-38f7-9861-dde5f6554a68 | -12.02367 | -46.02386 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 642603fe-79b2-3d6c-b36b-9ba653ec3bbb | -11.8122 | -47.67849 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30ee2569-a8c5-368e-b9e5-987ce66b2972 | -7.12142 | -42.78771 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 601b64e6-c426-3d0f-b01d-2f4445678c79 | -4.86991 | -44.3082 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0756064-75ef-33f6-b712-84d5ed9bd319 | -12.5907 | -47.93651 | 2026-08-26 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 587059c3-ab93-3fd9-a369-b1b9f6b9f811 | -14.62019 | -42.532 | 2026-08-26 03:49:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3d7e58d6-9ca6-37d7-8c79-54b3e8ba0b2c | -13.33382 | -48.22019 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36714c8a-ca4a-3b4c-a360-ad2595d20a9f | -18.54498 | -42.57582 | 2026-08-26 03:49:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fdc3a146-0423-3cf7-83a8-e47705cd6afa | -12.03608 | -46.03493 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 976b584f-5e07-3b3f-90ad-06b4ec7f4649 | -10.9122 | -44.73668 | 2026-08-26 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85d4cb08-7584-3726-8215-09fdbeaaa8f7 | -7.08984 | -42.17924 | 2026-08-26 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 411c597d-4efb-3575-848e-552c33b149f1 | -11.49042 | -45.11461 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecb2d6d4-fb65-386b-9061-6a465de1a73f | -12.7683 | -44.26038 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79458dc6-8428-3846-9324-7ef607e791c5 | -12.682 | -48.40065 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed825e3e-7158-3dc9-b871-2864ef63f8c7 | -5.33892 | -45.15788 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b08f5b5c-3b63-3fba-8913-c35f01c77391 | -11.25665 | -47.05608 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c34c99e-de37-3b0b-ba44-c4d903601740 | -4.84747 | -44.29493 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c18a8c9-8ea8-3365-832b-7225e9acb607 | 1.4917 | -55.9837 | 2026-08-26 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ecd59ef5-b1e2-338f-930c-ad7ee25e7100 | -6.641 | -58.4987 | 2026-08-26 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| acc4f06e-4843-3c8b-afe3-a8a19ed06829 | -6.6409 | -58.5181 | 2026-08-26 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c3f6997b-007a-301b-af0a-a27399a81352 | -10.3727 | -45.0537 | 2026-08-26 03:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 31c98329-d447-35fe-bad0-b46f3e4015db | -6.2676 | -53.3768 | 2026-08-26 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 25d59d2a-d075-3dff-8d34-74eab37680ff | -7.5289 | -61.3825 | 2026-08-26 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 80006929-b40e-3147-adef-0092459162c9 | -7.0613 | -59.2165 | 2026-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6c6897a5-229b-3bce-abe3-9d84d125c2ab | -10.7784 | -54.0368 | 2026-08-26 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 35f9e025-b09b-34a7-886b-ba2a3259c879 | -7.0612 | -59.2358 | 2026-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c0b8a94a-1e2c-3657-af0b-5096725ec99d | -7.5288 | -61.4015 | 2026-08-26 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 97379224-be31-38c9-b49c-4d52d9b1b777 | -7.0242 | -59.2374 | 2026-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fbe1b99b-87ee-367f-b1f3-73e7fb828966 | 1.4734 | -55.9839 | 2026-08-26 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| db25dd6f-41ed-337d-98ef-d7edfe5f432c | -10.7596 | -54.0384 | 2026-08-26 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |


[Clique aqui para ver as próximas entradas](README14.md)
