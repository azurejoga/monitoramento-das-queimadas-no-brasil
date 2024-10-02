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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc0275b6-07bd-3d05-bbd9-fd6ffeeaabd8 | -11.87639 | -43.81413 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7cc5805-e105-3d9d-9bb7-5c646ff976e0 | -11.26969 | -43.3847 | 2024-10-02 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5284a596-fca3-38f2-891a-61a3debc6f77 | -11.2689 | -43.38937 | 2024-10-02 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 352b8f2b-ef4d-3085-a99f-06cb9aa009fe | -11.26593 | -43.38404 | 2024-10-02 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dee00a88-7bd6-3852-a2b8-703eec20d8ce | -13.57998 | -44.77485 | 2024-10-02 03:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de439227-9052-3e97-914f-f01b07fd64fa | -12.99188 | -44.72347 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3c68a18-2d3c-3c1d-851d-237bd81e7d1d | -12.99125 | -44.72703 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9592daab-5e5f-3edc-a604-3e6f95847cee | -12.98791 | -44.72273 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f90edf7-5f26-3662-b0bd-775bcd49c69e | -13.11079 | -43.50116 | 2024-10-02 03:53:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54aee2d-7b40-3f4c-bba4-06eac07884b0 | -13.11002 | -43.50565 | 2024-10-02 03:53:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f9e0641-e6bf-306e-9eee-8d38977c14d8 | -13.0213 | -43.75306 | 2024-10-02 03:53:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a96d90b-b968-302f-9af6-756692eb725e | -12.44208 | -43.73116 | 2024-10-02 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10522267-6e7e-32d5-99b7-fa626bc49eee | -12.4391 | -43.72575 | 2024-10-02 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6f919a6-609b-37a6-a0d1-9ac64d094230 | -12.4383 | -43.73046 | 2024-10-02 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a6c6c0a8-722f-3fd1-a20d-abfb109f1930 | -12.4375 | -43.73516 | 2024-10-02 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 13291fda-690b-32d6-9228-6c6962a2f17e | -10.79256 | -45.55816 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7373ff36-bce4-3278-bf10-ea816ba4d75b | -10.79179 | -45.56254 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae0bc09c-a306-3177-a792-5f62c1e12f7a | -10.66771 | -44.50331 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b78c7a9-841f-3a4b-92db-a685971f0e1f | -10.66364 | -44.50256 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7a72ef-8ec2-3b9f-8091-629b7c825769 | -10.65957 | -44.50182 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 37ceead3-0962-3dcf-bae4-cdabf39d9bce | -10.65551 | -44.50108 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8b8d036f-be4c-3387-8c7c-b9deacc855c0 | -10.43301 | -44.90945 | 2024-10-02 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e2ce8bb-fcfe-3bb5-8483-9638ee14677e | -10.422 | -45.27157 | 2024-10-02 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ad61cb7-e7ea-3c0c-bf7f-d41815b95bef | -10.41771 | -45.2708 | 2024-10-02 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf7593c-e1dc-3c12-83b2-4c9266230003 | -10.41701 | -45.27481 | 2024-10-02 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bf77150-0554-3133-bac0-41e2093c71bd | -10.04854 | -45.64375 | 2024-10-02 03:53:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51b1069e-f4e2-31fb-abc2-a8c588a65458 | -12.09164 | -44.99042 | 2024-10-02 03:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8487a309-d429-3c9b-af37-21191370dad2 | -11.73194 | -44.96457 | 2024-10-02 03:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df85e21b-2e12-31a1-a4e0-11242c0f93ec | -11.67299 | -44.70674 | 2024-10-02 03:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af6d741c-0664-3d9b-8276-c9099940c099 | -11.16654 | -45.97526 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d9b2bb0-0323-30bb-b392-2caeda1e2791 | -11.14746 | -45.95357 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2ef2f1-eff0-3b30-93b3-581bc6c77edc | -10.87437 | -45.96875 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49945afe-f411-3945-b69f-b9ba75e28d5d | -10.87264 | -45.96683 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd32197-51dd-364c-a0da-ef0646a86016 | -10.8707 | -45.9634 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a333e30-1712-37b7-b425-2c649faf0874 | -10.86991 | -45.96792 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afe632fa-4b28-3fa9-bdb6-648f02b7c49a | -10.869 | -45.9615 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bdcc4c1-7e4a-37ab-9f7d-3750a54f14ee | -10.86817 | -45.966 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88947f6a-b085-3979-88c5-2b04c6c3112a | -10.86623 | -45.96257 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18e176f2-6ae8-314f-84cc-a81df7c01d29 | -10.86454 | -45.96068 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30974e46-5de4-37f2-9748-a847d06905b9 | -10.86177 | -45.96174 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05df968d-88c1-33c8-8bb3-f2089a7005f2 | -13.16919 | -46.31239 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25075055-8721-3891-bdd3-0092ff83e6ef | -13.16657 | -46.32693 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76aae42-20eb-3659-9c05-5bbb33c28351 | -13.16575 | -46.3315 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff74edc-9e7d-30b6-9b76-603df9cc2530 | -13.16136 | -46.33057 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c255ab66-388e-326b-8b25-237dca2c1f3a | -13.16056 | -46.33503 | 2024-10-02 03:53:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a616cfc7-ec12-3aba-af61-e14fffbf3643 | -10.32224 | -47.4605 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b68c872-6124-3024-a16d-ec7e02e85337 | -10.31725 | -47.45958 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65a977fe-12e0-3960-b2c5-3c4d33b3b974 | -10.7124 | -46.17156 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 033b5581-fad9-36ef-b9e2-91d8fb3977ca | -10.71157 | -46.17606 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcefd236-1105-372b-bf80-98a1c6a18cef | -10.71144 | -46.1739 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be87e473-278b-3856-b87a-fcdeeaacc52b | -10.7077 | -46.16853 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ef399d0-f663-3fa3-b9ab-b9621f254cd5 | -10.70396 | -46.16322 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 699f43c6-1a88-3229-838d-c1f2aa1ed381 | -10.69945 | -46.16217 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7855ff3-551d-34f8-9d31-3b0e9a47021a | -10.69495 | -46.16113 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb4f8b7d-0a5a-3f6f-ae13-7b16eb86e43f | -10.69123 | -46.15567 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e4e2b79-f6e2-3bb7-b21c-540d24150822 | -10.68752 | -46.15024 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae3a19a8-6281-3106-bc56-b5842005f452 | -10.68672 | -46.15471 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0134d771-7f9e-3a0c-99ea-dbe2e33ee612 | -10.68379 | -46.14486 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1c4680a-abb0-3ccd-823d-3566411a95a1 | -10.67927 | -46.14394 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8042693-2d93-3873-a4c0-97eba818fdbd | -10.90883 | -46.33563 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb4d403e-0a2e-30c6-bccd-2521190142e3 | -10.90845 | -46.33965 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01ceaf61-9510-34df-8f97-cc953b9b0fe0 | -10.50757 | -46.31067 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5544fdc-2676-3d30-8026-6fd17b8de476 | -10.50497 | -46.03551 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4714e5d6-59e7-3957-b877-ca024ac7e01b | -10.50044 | -46.03477 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35a6beb5-2b23-34e0-ad9a-b180eabae766 | -10.49591 | -46.03403 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee6d362-9dfd-3a2a-836d-67b763d44aef | -10.49554 | -46.29844 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95787c31-4075-392b-82db-1d5ff4bfdb91 | -10.21569 | -46.82987 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b93d297f-f822-3bc7-8a3a-d46334dcd083 | -10.124 | -46.32288 | 2024-10-02 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8608174-6999-39e8-b634-e7ff74469cb0 | -10.08236 | -46.85831 | 2024-10-02 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 903b994a-f0b0-338e-a6b7-35f2732c2f7a | -10.07754 | -46.85748 | 2024-10-02 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 892749eb-0209-3a23-9963-f587e1e9744c | -11.34068 | -46.26874 | 2024-10-02 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bdcdff1-2667-389b-b5f8-ad125e718066 | -11.01242 | -46.51862 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e3f7d99-35e5-3909-8695-05f7483b7f4e | -11.0087 | -46.51283 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b74ad9c3-0892-3397-aeb5-55c0c8580a61 | -10.99642 | -46.4546 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3369fbb8-ecc8-31d3-8c5d-ed1e1301604a | -10.99267 | -46.44895 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e67dd99-31c6-3ffa-b3ec-8f5cddf509ff | -10.99178 | -46.45399 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa05f6ac-289c-3193-9ef1-2ceba9cc5d85 | -10.98706 | -46.56166 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e239fa-218f-3ca1-a1ba-f715488d0db9 | -10.91778 | -46.34027 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28a7bd49-8395-3bb2-8980-b970a7b525c3 | -10.91726 | -46.34119 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22f4c024-d887-37c0-afec-adcdabe81b01 | -10.91636 | -46.34614 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecde3082-603f-3076-9aa4-1e65268d5357 | -10.91605 | -46.35011 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2420a1cb-2e3f-3882-8616-520877c45ec8 | -10.91436 | -46.35972 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8e49cd5-100e-3077-93a2-b36b5f479fdf | -10.91371 | -46.36055 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25b14586-3b3d-314d-8da1-0aa8b2b0981f | -10.91349 | -46.36472 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50fcc5da-71e7-312c-b6e1-a31815b504c4 | -10.91307 | -46.34022 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a3a0b0f-db67-3b98-843a-b566c2f60fd8 | -10.91278 | -46.36561 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4ffd9d7-18ef-306a-b703-040173916bf5 | -10.91255 | -46.3411 | 2024-10-02 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e248e89e-b5dc-3641-b1d7-7ce0a472e251 | -10.94549 | -47.29202 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 434abfb8-5eae-3818-895e-8e270ee332d7 | -10.94368 | -47.28729 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e33d9266-172e-3893-a6f1-330f97251a7f | -10.94257 | -47.28026 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f2b236b-a44a-3b36-9eb1-cf73e229824e | -10.93983 | -47.28094 | 2024-10-02 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4de920a-cf99-361c-b388-b507f2fe903a | -11.82541 | -47.30133 | 2024-10-02 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1896614-a5cb-34da-9b2e-75312c62e1bb | -11.76369 | -47.61392 | 2024-10-02 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 334955fd-c5fa-3e95-a5c3-faba29dae379 | -11.76034 | -47.6129 | 2024-10-02 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e43e6eca-b0d5-3ea4-b723-42eba8b40748 | -11.7588 | -47.61285 | 2024-10-02 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdce5755-3a1d-3326-a310-6ecbc2157caa | -12.47799 | -47.50129 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c62c5e-71ad-325d-9922-cbe0a763d764 | -12.47697 | -47.50674 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8500596a-042c-3f8f-83a6-a4000f53a0d2 | -12.4742 | -47.49494 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0724ac5-dead-3c81-90c8-b37acfac52ca | -12.47318 | -47.50036 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ec8f68c-b4fc-334c-9f81-fcd5f32fdc51 | -12.29612 | -47.65051 | 2024-10-02 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README64.md)
