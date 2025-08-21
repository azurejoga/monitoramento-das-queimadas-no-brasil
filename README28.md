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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a961d6d-70ad-39f0-8c9f-9c3365f77d95 | -5.96834 | -44.14102 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf0ab66d-ce0d-3339-b82e-eb9003c547fa | -7.28222 | -49.39954 | 2025-08-21 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc014969-4327-33d7-98fd-47bc8557c82a | -5.80169 | -45.00627 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6e55285-f9ae-3d8d-abc0-0c109e1551b1 | -11.51764 | -50.54436 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1afbd76-da18-3d91-b290-6fef90858018 | -5.98704 | -42.84779 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bb62d14-0c51-37b4-9d6c-296ca40cbe95 | -12.09289 | -47.90243 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b389ce11-885f-34c0-898e-71389f5cabb7 | -7.30683 | -43.68062 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d2b05db-90dc-3cb1-b269-3527745fb5ed | -6.71861 | -44.3259 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ceabb96-7728-3b5b-a1ea-7b8122ac7979 | -7.99389 | -47.3406 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43eff2e8-7624-3480-9b18-3c75d4c8f74b | -5.47695 | -44.70033 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 375f9c1b-7249-30dc-9a14-067b2f69ceef | -7.6625 | -45.24742 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55e932fa-67ae-39af-af92-8f935f89b0ba | -10.28026 | -46.77976 | 2025-08-21 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba94b160-c6e9-3412-9f44-1a4bd2b8e7a8 | -5.87543 | -48.11781 | 2025-08-21 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64752314-c41b-3e53-abbd-290f20d63455 | -7.21128 | -45.31251 | 2025-08-21 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5a905a3-79a1-3449-8e69-7f9e688c1976 | -8.16267 | -47.32938 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f4025ce-1a74-33df-9461-75a7e4b2ac69 | -4.94034 | -47.4613 | 2025-08-21 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07f2c727-c6d3-38a4-8d77-361205a0939e | -7.23669 | -44.7093 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe1c6eb7-79d8-3ab5-b4ef-b303b11de839 | -13.32942 | -40.34434 | 2025-08-21 04:17:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 30ff8c61-d955-3009-8e19-50ff15382a2d | -6.03457 | -44.38434 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74576f5d-4368-3c2b-85e7-1820a1329311 | -9.85649 | -44.69048 | 2025-08-21 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cf19199-31fa-3659-98f8-88143a5b4c92 | -9.4818 | -47.32645 | 2025-08-21 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e5180ed-cc5a-3729-aaa1-e8fb54b5354e | -7.64319 | -45.24517 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 621216cc-5d33-35f7-aef9-2a26ef6ce81d | -7.60985 | -44.38757 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ad95f7d-7a6d-32ea-9d7f-75a1cef5b8de | -6.01943 | -44.34856 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae87fe9-6fd2-3adb-983b-cf50259e61d0 | -6.06757 | -44.11244 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09b11684-86e1-37f3-bdda-f583b250483c | -5.82484 | -51.68974 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a44ff67-d99f-3c6f-873e-b2d565256dbe | -8.28936 | -47.28653 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2013750-7d9c-32d4-96d9-24e3768128f4 | -9.36013 | -48.29095 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d7b2302-ad75-337a-aa59-a377056ee754 | -10.72075 | -48.23384 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8b06f51-eaec-3ab5-8509-247f4145f4e6 | -6.01255 | -44.36976 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91c5bcc9-a7f6-3b47-8d0b-db3e88b75f91 | -7.38575 | -45.98781 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb51c2d-45ee-303e-b557-4125f4af1ee6 | -6.95497 | -42.86555 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f16b1d6-7fbf-305f-8215-8eee55307715 | -7.61763 | -45.27202 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03812156-c32a-35d4-a9e9-9b5a6d6b06ea | -7.58969 | -44.38424 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dc316bf-9441-33d5-b8d2-b6d4058c19a7 | -6.10473 | -45.4101 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eba89afa-cf88-36a1-a3df-211752d76c66 | -6.29328 | -43.88257 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 175e45a0-f03c-3539-8026-5b2fe0159aa4 | -10.72099 | -48.24113 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc4da34b-5a18-38ef-a5d0-33d6a964e4ce | -6.09916 | -44.63433 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50fa2e32-8e0e-3736-8383-2a8d8155cc27 | -6.02332 | -44.36769 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9fbcc9b-e18d-3d76-8931-cceb43c33c7b | -5.89819 | -46.16006 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae9adb7-8453-31b5-89d7-306d9cb6ac13 | -10.71881 | -48.23095 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 785da9c5-1e97-3e05-982e-cdad6c19a6d3 | -7.61478 | -45.26774 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee54fbc8-2c0f-36ad-898b-725c5735d7c9 | -6.10467 | -45.40908 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93929982-f71d-3b00-87e0-a0d6cc722f28 | -7.95019 | -42.65048 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74603ffc-1c2a-315f-b523-63ae47274cd9 | -7.72365 | -46.61483 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9317cea-21cf-3c43-8652-0c81ba830702 | -6.00974 | -42.85491 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ef38fc5-7988-3627-a5a5-ba2e582d2aaf | -6.44737 | -53.37507 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35836766-2117-3a16-a739-9a150e03cbf9 | -8.35012 | -47.50478 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfb3255a-3ced-3283-ad78-40b258e7716b | -9.91862 | -49.24708 | 2025-08-21 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdc372ed-b1a1-3dcb-a907-ecc0167c658b | -5.65467 | -43.3676 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b52959ab-0dea-345c-8128-a578b2ee083b | -4.55336 | -50.45947 | 2025-08-21 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7efca564-7005-34b9-978e-2275373a21db | -8.03275 | -47.68225 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cf742cf-735e-3094-8319-bcf111ae38a7 | -8.49534 | -45.69242 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d253ce92-8277-39ca-af1b-f9e1ddf61dbc | -8.16586 | -47.35103 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d03cea67-0c35-372d-a275-430d866f552c | -7.65186 | -46.25797 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b12dbee-bf15-3c93-aa66-76031b6819db | -11.32501 | -47.83836 | 2025-08-21 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a58e77e-a330-3dee-ba9c-4980684774b5 | -6.42253 | -44.66655 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31440918-4a52-3f3b-9f48-104c95b68e69 | -12.20661 | -45.43627 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6c5244b-70ce-3e7e-a21f-0e63cf2ff66f | -12.07818 | -47.91142 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3562321-d686-3a90-8954-bfdfbb8bfd9a | -10.72379 | -48.23932 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47e8eef4-a257-38ee-a6af-4faf57f1ecc1 | -7.57393 | -44.39636 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9e65be9-7134-3485-b098-02665754eae8 | -6.73288 | -43.9929 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeaf3d7d-cf86-312e-a660-bd98b89ffde4 | -6.54743 | -43.99177 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3928514-1263-3a84-a5ae-63f41e215da9 | -8.16048 | -47.35963 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 11e2e7da-deac-3d79-a3be-169d4349c8c2 | -5.75432 | -45.29958 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67b5344f-295b-35fd-a8d2-5d4210c9509c | -6.27239 | -43.71315 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c50b6b6a-b0e3-3c34-b694-67728708d546 | -6.49267 | -42.97028 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4a48dfa-97e4-3608-9bcb-a045f408e876 | -5.98481 | -42.84034 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3ce7b46f-8350-36af-9692-49b02d03c52d | -6.96436 | -44.16722 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eae64626-6560-3093-b52e-a26cc231d466 | -7.02079 | -44.61831 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4a88df14-b074-3770-b83a-9859b8cb1451 | -11.81332 | -44.2618 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7123f2a-388f-366c-b99d-9994e01ca373 | -11.818 | -50.65308 | 2025-08-21 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e1da23-1240-3498-979b-a6353eedc501 | -8.16507 | -47.35564 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c647a57-ef95-3c3a-b7b2-8d6d233cb6b8 | -9.66159 | -48.381 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fcb0861f-71be-3211-977b-e1fa52eb28f8 | -7.72295 | -46.61911 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fa5c24c-fb05-3b45-b75e-13dd76efa9ad | -8.3792 | -54.99643 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed0885d-a2d4-3073-8ab0-66c6c87dd2f6 | -6.07087 | -44.13511 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4685694-e753-35e9-a022-2d292cb388fc | -7.63507 | -45.25167 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 888bc46f-25b2-32e7-b31a-1a9b500af5ec | -8.83707 | -52.05138 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 677ef03f-d11b-3431-9e57-1ee54adfb9f5 | -5.78427 | -45.06998 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24e6a532-d6e4-360f-a1c1-833f84c93770 | -6.06991 | -44.38219 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34931b2e-4312-36e6-ba96-30acbd304c1b | -5.08936 | -47.71484 | 2025-08-21 04:17:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42839118-fbdd-3371-b287-3695f9b39165 | -12.08916 | -47.90188 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a2faa17-5b8d-3a89-91da-b2a8b4bf63b1 | -8.28593 | -47.28374 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a35c6f98-8b93-3a36-8450-8e71889e0155 | -5.59688 | -46.29215 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d0e5cbc-2200-3b81-b9b5-c783153e91d5 | -7.14352 | -44.1775 | 2025-08-21 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d5cbcce-23a4-39cc-a2b4-4c93b893d418 | -6.07612 | -44.38686 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e47ce8b0-d3e6-31f8-9893-42a1164f16ff | -9.55822 | -48.11819 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25791bf8-92da-30c9-bee5-4c6ebe833ffb | -6.26375 | -52.82292 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53cd1a3f-24fb-3970-88ff-2d4632f0f16e | -5.95874 | -44.15789 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37535d6c-c68b-3079-8b75-e880f84b2e00 | -5.6452 | -43.72175 | 2025-08-21 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8534328-dd7d-3d1f-97ad-cbc7a3d24948 | -11.81437 | -50.64786 | 2025-08-21 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbe71961-c101-3016-ac0e-109938417903 | -7.65403 | -40.41901 | 2025-08-21 04:17:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a2204b4-763f-3a4e-a21e-d909ffed6ab6 | -13.02718 | -45.15843 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 130954de-d974-3dbe-aab3-2dcdf9590f50 | -12.07938 | -47.9142 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ecd3a6c-d79e-39ed-a770-6b329ab69a97 | -5.98371 | -42.84727 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b4d1992-50fc-39e2-a730-f00aa4ac4844 | -6.94999 | -43.86084 | 2025-08-21 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee82d448-6455-364e-90a5-b65b14da64bd | -9.31561 | -48.93416 | 2025-08-21 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73b70a7b-d740-3730-90df-7e326ff12c1d | -6.27182 | -43.71667 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b80250b3-15fd-3b43-85c4-a0e0db7d5c20 | -11.76002 | -40.18834 | 2025-08-21 04:17:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
