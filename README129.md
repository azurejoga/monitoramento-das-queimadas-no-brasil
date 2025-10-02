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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbc3d9cd-9df7-38e8-ab59-05cfc3b6ab94 | -13.15751 | -47.83157 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18b4ebf8-2ded-3940-a152-9baf55de58db | -10.9299 | -48.58558 | 2025-10-02 04:51:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 701a6bcf-e8eb-3d6b-a0ae-c9341088e5d2 | -15.39795 | -49.20174 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56b93cc2-e4b3-3132-923a-c2f5f27ea50e | -14.88741 | -48.12413 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9174295-e20e-3caf-8b7e-ec5126651e12 | -11.17507 | -47.27613 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cf03b1b6-c22d-30b0-babf-e00e30261c87 | -10.83192 | -46.62409 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b54c774-a73f-3390-8804-bec1eb4b26f4 | -14.71589 | -48.20807 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bc072d-6546-3570-8f1a-e6c15c8d2863 | -14.21727 | -46.11036 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f2c753b-1d9c-322c-9026-f2454f8317de | -11.09047 | -47.80876 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03b659d3-d2a5-34b2-ae16-513cbe62a990 | -13.29768 | -47.21471 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ce5be01-3c61-3d0b-b178-8129c971698b | -11.85356 | -48.02549 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 168fd85a-bca1-38c2-b4a4-c2c92fd452fe | -14.86551 | -48.29033 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b45f3a1-7351-3d1b-a997-20203fb6c913 | -13.75586 | -47.95 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb49f62a-8875-3cb9-9bf6-725ebb6b81d1 | -10.81949 | -46.61271 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7ed641-03bd-3f4a-a9d4-42a4b54f908c | -11.28993 | -47.83119 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfba20af-fb04-3e0c-a5ab-347b01937163 | -14.60215 | -48.32545 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf92655-b990-3421-80f7-3dd8e1b75731 | -11.66946 | -47.50198 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85b07c8e-d670-34db-b6d4-4bb86db48af7 | -11.67276 | -47.49942 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3114a1c0-3187-35f7-b1da-976ef7a5e9c0 | -11.60376 | -47.2235 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 024b28a8-95a0-3ffa-bb95-feddf3388766 | -10.26371 | -50.32315 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b34be54d-5160-3d1e-a8aa-218c164f526f | -11.46622 | -45.02282 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be78b917-d759-3180-aee9-92b286e6a2dc | -10.84436 | -45.38616 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 085ee28f-e3c8-30e7-b2aa-ec4eddae2f97 | -10.82072 | -46.60337 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71923aee-03d4-380d-8f94-7508f23cf8f3 | -11.10574 | -49.80488 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bac498cf-a847-300f-b3b8-34eb37d5ce0a | -9.93916 | -43.72034 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e165ebdd-2783-3b14-83f1-263ca862c1f5 | -10.30977 | -48.24623 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b354b736-1865-3822-8543-c430d779a855 | -14.64985 | -48.26184 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 512431b4-de57-347e-bec9-1f66cf4cca07 | -13.31022 | -47.85648 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5670c1f2-ba9c-33de-9276-94f21e2800d1 | -10.99417 | -46.59758 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a4c00373-068c-3ae4-9bf4-f4896c0d11a1 | -15.35921 | -47.0681 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb77aeb8-8aae-3136-94ea-01fc831a7c50 | -11.80604 | -44.99416 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fae97e1b-3c78-3a50-8907-63819e938249 | -12.25799 | -47.81007 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 159d498b-ca3f-3449-bd24-b053e6492fbf | -11.43394 | -47.18346 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83396484-5662-3e1b-88c9-d6a0b1b808bc | -13.00588 | -45.21115 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe960b16-3fa7-3433-b868-e29de97181a3 | -13.80762 | -47.54284 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ee4d4105-bf31-3c1a-ab9e-f04c77b17904 | -9.40643 | -47.55345 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 208bef43-f828-3352-a54b-50ca01eb86e4 | -10.83524 | -46.63403 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03f9159e-a61f-3fd7-9497-528a75e21e1e | -13.00627 | -45.20799 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31a4d9a3-25ab-3ac5-ac28-ae345ef85b45 | -11.10995 | -51.06541 | 2025-10-02 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7baa8c1-3d8a-3089-88fd-46578b4317b3 | -10.06077 | -48.18835 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f775c70-9523-31b0-81cd-a51881eb4e0a | -13.16057 | -47.80824 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41193322-f06d-38b7-92ca-4882a16ac02a | -10.82282 | -46.6227 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44e783b6-eb46-321d-bd3a-6741fe1d16f5 | -12.71089 | -46.88818 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1356e791-b983-3e39-bfda-8a3b95a103c3 | -13.55486 | -47.28664 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 576c83fd-614a-3c53-b62b-c5c0d6909a98 | -13.80429 | -47.53315 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c8ae7de-4aca-389a-b519-a131449d6ceb | -10.22508 | -48.22758 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95ac038f-56d6-3fcd-977c-358a5d4064af | -10.86948 | -47.81909 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91156669-2773-3392-afc0-8d2ff346cf2c | -10.84362 | -45.3917 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1cb9f3c5-372e-33ec-9cc5-b4c4464f8135 | -14.02656 | -47.99708 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f649b317-0004-35cf-a86f-5823b4e0b696 | -14.89557 | -48.09578 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba1adc24-5e10-3927-8666-9e7b2dea402c | -11.17772 | -47.19118 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e60cb08-2641-3235-9ace-462b913ec8e4 | -14.46872 | -48.42382 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22ad92f2-8ea8-38b4-a4d1-ddf9a6271b18 | -13.15684 | -47.80293 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7daa3e53-aced-352e-9c2e-e8c8918b60c4 | -13.19198 | -47.83825 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d072739-23ff-341a-b849-3773f6e7196e | -13.30808 | -47.83944 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6f3926a-78a7-3092-9a23-678ea1b07857 | -10.2709 | -50.32423 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 986d05be-c95c-3337-8da3-868c00b37410 | -9.94557 | -43.71383 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c0cb88d-722e-3f65-8e15-6cba018b0eb6 | -13.75095 | -48.00766 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 919adc66-300e-3ce2-a66e-fc95a78a07e1 | -13.86278 | -47.95282 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11ae1bfe-adc3-340c-aecf-a404b6e51c15 | -11.27209 | -47.80465 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 285bc2c3-208d-3bb6-8dd6-909fe0acf4cb | -10.81852 | -46.61624 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c847c8fb-5187-322d-bd04-a50212669405 | -13.53574 | -47.25573 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41658ee6-3ec5-3a0e-98ed-6d149755d2e9 | -15.25594 | -56.77736 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8bb0748-d974-3f1c-93cd-99fc9bbca36e | -10.27028 | -50.32838 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 01c1a4c1-2195-3c82-9de4-5056e1aaf390 | -13.80899 | -47.54466 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e5a76eeb-8dca-3eb3-bb4b-da660c609dd0 | -13.91761 | -48.07355 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c694114b-2d6c-3a99-84fd-e20fd86f2f20 | -11.87662 | -51.22835 | 2025-10-02 04:51:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69360e0c-b8c9-3968-9610-d2ba2107cd3d | -11.13152 | -43.39103 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac1d31fa-e490-3099-8d0d-1fb9eb73974b | -11.82838 | -44.98367 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3382ff29-375d-3a81-8137-3287fc26dd2d | -13.15135 | -47.84491 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df3c75fc-f5db-3415-b1ec-77aa0dbcf598 | -11.59529 | -47.64558 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5bdf329b-1f5e-3b19-b184-18ee39c4e23f | -16.04402 | -50.88375 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b3f77490-eddf-3d5c-a2fb-29956fef57c6 | -13.75477 | -48.012 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce60c059-3e9e-3d15-9ae3-7916ba8a7b6c | -10.2512 | -50.30853 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64f1fcdc-f4a0-3475-a412-c83b47e28a91 | -9.93692 | -43.73795 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f3039c2b-e6ef-3b19-b8be-b17ea38c0a82 | -11.80568 | -44.99708 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 927c2a2f-22a5-3cf9-b82e-3da0f501234e | -13.30588 | -47.85588 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66e96978-ab07-3ddd-912b-644e61e75252 | -12.94281 | -46.43072 | 2025-10-02 04:51:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c7dbec1-e458-3897-9109-094ca190588d | -10.95922 | -46.64987 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 654c9cba-4c82-3a61-a15f-a222568dd348 | -11.61572 | -45.05795 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b69a6e-0069-335e-90e1-0dbe530490b3 | -12.12587 | -43.4309 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da4fd101-1a73-3898-a746-64a08eef6490 | -14.44279 | -46.34247 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 822850c0-2bb4-36bb-afd0-aba4a4e1d19c | -11.1382 | -43.38407 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91a9c927-4993-330a-8a26-023656fae050 | -13.01145 | -45.20865 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7db0ecb-bc9d-3060-a462-7630a6e2a00e | -13.01066 | -45.21497 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e17d37eb-5702-32f1-83d4-71701694c304 | -13.78005 | -48.00191 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c435bb0-079b-38b4-8c72-3def0aedb789 | -12.26169 | -47.81491 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f725957f-da2a-3a35-8e02-3391ba7b7dfd | -10.95858 | -46.65465 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aafa43bf-7b6d-3855-8ba2-9762a7afc23d | -11.03254 | -47.82302 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33e961ea-78cb-3df9-8482-47f2a6a3013f | -11.79495 | -44.99896 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 270ed518-f751-3121-83c0-5b50e85e0837 | -14.86977 | -48.29131 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a5eb1a-a70a-3e49-8eb3-b727b3ea2961 | -12.81089 | -47.01596 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3802abfd-2259-3dd7-a984-53f072d5fc4d | -10.8602 | -45.41859 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 374a945e-5b46-3764-b960-a04ddd956611 | -11.15072 | -54.1192 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1210611b-7e0a-3656-a0fd-bec40089f425 | -14.37148 | -45.96797 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22b66b1f-7bb5-30f0-98dd-50823f0fca2d | -14.58501 | -48.32304 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| db8661b4-7b14-3db3-b0d8-9eb06100b466 | -13.80126 | -47.53448 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 015f9a54-552b-396f-9e69-77bdf5650759 | -13.94116 | -48.09453 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b1cb1a4-22bf-3577-baad-de061141789f | -11.87253 | -48.01226 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae154a1d-7b4b-39dc-b4ab-33639b859644 | -12.11545 | -43.42034 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README130.md)
