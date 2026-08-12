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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f56b82f9-45cf-39c0-bf10-a3bc849ad532 | -9.34793 | -47.4946 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71298af9-b6bb-39e8-996a-24e8b9f1dab5 | -8.94295 | -60.51008 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad73c8a2-e1e8-3916-b212-7ee2bf266508 | -13.85846 | -53.82152 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a3ac329-e291-3b00-9e28-684c87d9deb4 | -11.93747 | -47.35191 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83aed8fe-2d39-37c4-be5e-2c80fe12c07e | -14.03758 | -53.59975 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf3f9176-dc89-3788-b1f4-4aa946945d66 | -15.00444 | -46.60088 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 350d8451-5be0-3047-b55e-dc8176371f0f | -13.8326 | -53.82518 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f2fab0d-5df9-3763-b271-1b2558dd2b9e | -8.95091 | -60.49926 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80097e4c-1047-356b-aaaf-b353ebe9fe4f | -11.95091 | -46.35138 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| de821deb-5799-3135-93ac-0048bfa1ec31 | -15.16804 | -52.77794 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f0cdd9-76c1-3287-b046-79f67f89dd4e | -9.48038 | -47.83011 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3ce34fb-e57d-3155-a120-ce6016c950af | -11.81813 | -51.83284 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8d9f2d45-11c4-3b59-8b8f-f08d83908b02 | -11.81557 | -51.89141 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e86a4d8c-b856-38c5-9698-7e54e8a49966 | -13.89791 | -53.80252 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 432b897c-d389-332e-81af-c22043ab3d33 | -11.82136 | -51.85548 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea89ff8b-1e43-34fe-a3c2-bf0857bf8613 | -11.98894 | -46.36406 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2523cf18-79d3-3efb-88bc-27e18221800a | -10.71286 | -47.91803 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f729c3ef-80ad-38ad-bd04-2ab585960ccc | -9.36181 | -47.45125 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcf62a4c-398a-32c1-a69d-f36f354f47ba | -15.51787 | -45.85741 | 2026-08-12 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5046cc78-b90a-39a8-883b-3b0ec201fc70 | -15.30572 | -48.87999 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d950df96-b516-3e6d-ba2a-f2e4750bcc85 | -15.30277 | -48.87542 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f765581-5e54-3f13-b36b-6a57550bb572 | -13.28732 | -49.6915 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbea082c-e996-3b68-9b28-fd6ad3b667d0 | -13.85565 | -53.81675 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50e46df5-9f10-3bb4-a4a5-bee493e5c960 | -13.90278 | -53.79514 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2863d173-a72c-3b69-a884-a535fd8357f0 | -10.82126 | -50.33352 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaff0b3a-712d-379a-ac2a-461d210cc7f3 | -14.52498 | -49.29532 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04e482e8-3e77-3914-bb10-98fcf3f8b59d | -7.40878 | -60.0012 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4da40d10-ab54-3491-95a0-35b7604690be | -11.80924 | -51.82399 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a84cd6be-0762-3fc0-b81f-22a78557b88f | -12.14071 | -48.26586 | 2026-08-12 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0600c5d-4f96-35dd-b975-7535e480dc74 | -11.82861 | -51.84154 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5952053c-c9cb-3899-b747-cdf4090b316e | -13.81907 | -53.90532 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e404c83-c9ed-3c17-88ab-e3987ffbb05a | -13.90993 | -53.83777 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d21572-9059-3239-b928-56844d55ccad | -11.80706 | -51.81624 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68aefe7c-9348-31fc-9ebb-d1c50f3b96b2 | -16.71975 | -46.40029 | 2026-08-12 04:51:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fbdf93d-b180-379e-9539-a87fe45acdd0 | -9.62042 | -48.33039 | 2026-08-12 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65653f7f-037d-37e9-a4c7-9bc6ba55be13 | -14.38127 | -52.0209 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8a1aaf8-7510-3a41-a4a8-39645be0912e | -9.36954 | -47.4483 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 127fe5a0-59fe-36cf-a186-3bbc30dac0a1 | -8.95441 | -60.51221 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 555de052-1349-37ec-b2a4-297d98d4cda1 | -11.97567 | -45.78897 | 2026-08-12 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a56826ac-aa43-3a17-abe4-3646078ab42a | -11.94903 | -46.33651 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 116fc4b6-2a27-3434-8bb6-41991954f765 | -14.98214 | -46.60741 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e004c62-fd22-39be-8ece-db5d20767ab4 | -14.53665 | -50.39011 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3234315a-0b31-34f9-bebe-0fdd3bd6aa9b | -13.59944 | -46.23762 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd437152-0874-3b7c-b43c-38f754cfb6a9 | -8.90049 | -60.57715 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 876baa8f-d2fb-3623-b881-490b31c1caeb | -13.90847 | -53.82516 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0ec3c1-9d67-3610-a256-75cdabc5a63a | -13.88649 | -53.82633 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d00f22-a132-3f65-acb5-690fd0b0204e | -9.76681 | -60.76334 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 526dbf67-6891-3ef4-a193-59c7d6bb424b | -11.95731 | -46.36243 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12c5009c-2807-335b-8e54-ce524d6d26b4 | -14.27889 | -45.2848 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 562996e0-3171-3b71-94fe-2c0a23931ccd | -14.52151 | -49.29486 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c60e37d2-5bb9-3c66-9006-a8e5286eadc5 | -14.99895 | -46.60404 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3ce1518-e937-3ee3-bf35-25e95217faf2 | -10.21673 | -45.93093 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 99e58762-3616-33d9-a5b8-ef93f5073eaa | -9.5186 | -47.4312 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d25a90-559d-3114-af45-e1328334cba6 | -7.40806 | -60.00506 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fdc0135-c438-338d-8402-c3d1eeb32000 | -11.78451 | -51.84933 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d261f8a3-1a35-359c-b172-1fdb34c13618 | -12.83242 | -52.02674 | 2026-08-12 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a10015b-8663-3291-9899-429c1b90eecd | -11.47728 | -44.56741 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6aada991-6854-3f34-8b76-9cd3ee62ea49 | -8.94868 | -60.51116 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47fca815-dd93-36a5-bf42-500f071f2687 | -7.41377 | -60.00605 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08135cb3-685f-3545-9986-f29b5ad689ff | -10.42384 | -46.32657 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1638050-2f7e-3559-a81f-dfa1a0acbe26 | -15.16625 | -49.26606 | 2026-08-12 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42a3adee-0357-317a-87ac-180d6d521d49 | -11.49599 | -54.60818 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 846b9a63-f0bc-3a01-8baa-026ae188b727 | -16.62093 | -49.42264 | 2026-08-12 04:51:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03bfc6c7-53aa-3958-b340-5f8a1dcfbcb9 | -11.95548 | -46.34728 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91b4f2e9-7c06-36a9-971c-78bfa2725372 | -11.80648 | -51.81985 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c090e67-b8e5-3e50-99cb-713761621dbe | -11.83951 | -51.88023 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a8e0f44-5ae8-32bb-b11a-1a1f7db05c21 | -10.22979 | -45.92364 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 089252d4-f7bb-32df-9144-8f6c40620d29 | -13.54034 | -46.27394 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4688fe07-7611-3af6-bb91-d914a28d2c5a | -10.43875 | -54.36256 | 2026-08-12 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46718bd3-94cd-3b3c-9afe-40aedcf35a71 | -11.47409 | -44.55834 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6888132-9ec2-3173-8c53-c6453b509452 | -14.44736 | -52.26043 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4d50fb30-c17b-308e-a863-e95308f998ca | -11.83615 | -51.87967 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e7721b8-cf72-3827-aaa1-c657c1d78244 | -13.54108 | -46.27522 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c30af7c-b3ac-30db-8cef-71510582533a | -10.82182 | -50.33001 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a08884e-8c35-3c0b-a4b2-1e4894c771e7 | -11.82368 | -51.84111 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be6abd1-4181-3384-b183-9444255ee4cf | -11.46768 | -46.61084 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 530f9946-a224-3610-8700-932fb19eac11 | -8.95531 | -60.57084 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bcb885a-58d2-3f78-800a-d19ffe4033ff | -15.30218 | -48.87941 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dd6d680-8049-3e64-8dcd-569c4d726cfb | -10.10403 | -46.20768 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8611d39-e3c2-31b2-8488-203acb164916 | -14.97897 | -46.60823 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f77cc7-dfb5-314f-a036-280348c22982 | -14.44402 | -52.25986 | 2026-08-12 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b56e515-86b4-3f95-ad80-bc038923b1ab | -12.31251 | -49.79446 | 2026-08-12 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6158c8bd-bfdd-38a0-a866-a56c1e205371 | -14.5512 | -50.39629 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96d9ff9b-5cd8-365b-bf4c-94962348e91e | -8.66182 | -54.96029 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efe99062-de14-3903-b1be-f3bfdcbaaa2d | -14.98435 | -46.59843 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e90fb983-ad1f-3c7d-940f-71b622031b91 | -14.50651 | -49.27644 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e71e9703-576b-3dbc-8863-f76a3ada5fcb | -14.03476 | -53.59529 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b0a1fff-68b4-3b8f-8bd6-c12dce353a94 | -13.57236 | -46.25579 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc698e63-63c2-349f-90a5-09063c038dce | -11.46102 | -44.55648 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00434f7a-2d3e-3b5a-a41f-b937bf507734 | -14.98037 | -46.59765 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4355c5a3-2e49-3017-bd4f-c043abb73a2e | -11.82626 | -51.85591 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d59c5a0-a6f8-363b-bb7e-7b5e753aff2b | -11.81259 | -51.82455 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cf825f2-fe20-3f65-b86f-4aa80c03ff9b | -11.95287 | -46.33754 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7db5aa23-e9a0-3da1-97c7-0959f7f0e7a5 | -10.09424 | -46.23226 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c67e6e53-6b87-38d8-a741-e2d9c629e31d | -8.9559 | -60.50428 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ce6447-2d46-3223-8d5a-0f4f03e61ecb | -16.34469 | -49.46835 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60d37969-cb88-32e4-97de-c010f325eb55 | -12.13913 | -57.19916 | 2026-08-12 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4836461c-2b09-3cac-b4b0-a3601355086e | -10.21599 | -45.93599 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d4c29d8b-8171-3e81-be63-2f3b5fe84635 | -13.88581 | -53.83043 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 436dc8a5-ca7a-32fb-be71-39e11f08e5c4 | -11.60787 | -54.65377 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
