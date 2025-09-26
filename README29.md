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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb5750f-e857-3127-9927-30d268f9132a | -6.8734 | -39.26511 | 2025-09-26 04:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fd02a66-3d78-3c6e-a6a1-fa80b3cf8977 | -10.40822 | -46.15848 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b96855b-36c4-3e58-93ca-eb0e3827ab13 | -6.6149 | -42.93261 | 2025-09-26 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b936d0-c336-3e14-b37f-dff4b17e6c6c | -9.76409 | -49.31393 | 2025-09-26 04:42:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef69c04c-b0ab-368c-8fd0-31af21022411 | -5.53702 | -42.81002 | 2025-09-26 04:42:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74f6aa30-91d3-33f6-a2c4-eafa49e8e27b | -3.78868 | -51.82853 | 2025-09-26 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80f47c9b-a87b-33dc-8692-95ec53cf5938 | -10.11499 | -45.33331 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d3a495-4ce2-342e-8eff-f21dc411018f | -5.21795 | -44.48954 | 2025-09-26 04:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5b472f8-c3b4-3b1c-ac0f-f29eb40dcf6d | -5.46478 | -43.05873 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b3c7ffb2-049a-313a-bca3-dd48e3cb51df | -8.324 | -49.52782 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2126364e-10a9-34b1-81f4-6229ae38bcde | -3.81829 | -50.97903 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 025f77c1-7129-3f77-bbdb-1cf7f1a22ffc | -5.73548 | -42.63445 | 2025-09-26 04:42:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c571ef11-a04c-32cd-95a4-f248f0065c21 | -7.58855 | -42.32721 | 2025-09-26 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 793621eb-8f03-3e69-8f75-907262d97ff3 | -9.69233 | -48.94588 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe4c4dca-88c0-3e23-aa2c-5502fe570e1e | -8.08104 | -55.22093 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 424e3220-8687-35d6-b352-5ced75e3efcb | -10.28795 | -45.22547 | 2025-09-26 04:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 963e740c-4436-329c-9ce0-bfd25672ceb0 | -6.29101 | -45.04535 | 2025-09-26 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5b01b12-493a-36d9-b8e8-8e2a01fcf358 | -5.47231 | -43.06857 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5e83bb02-8466-3ae0-b83b-a3b394d10ae4 | -8.78721 | -43.05636 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b886a264-9142-3bd2-a650-91218fb8bc32 | -5.46416 | -43.063 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 85772a57-e8b6-3058-99f2-eb354ed50604 | -6.26672 | -42.47493 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94d7c865-76f9-3bc3-81bc-9b8597e12cde | -4.69945 | -46.48225 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9559e3-b5e0-35ed-9d5c-8023c840f4bc | -4.31066 | -49.68808 | 2025-09-26 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0b6d1ae-868c-34a3-9890-6f945c19a8bc | -10.57131 | -44.08385 | 2025-09-26 04:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ea714648-b48e-38a8-9e7e-f8b702252390 | -10.11437 | -45.30866 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 847b2606-17a1-334f-b606-bfdb12eb63f3 | -6.85582 | -43.17915 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 57e13fcb-7e27-3f69-9c6d-1b5892b14b7f | -4.7573 | -43.60875 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e09689c-44a3-3320-846e-fbc5f53ac81a | -7.67414 | -45.99149 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5b65fe3-c1d0-34a6-a5bf-05d4212f89c8 | -9.54713 | -47.52286 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a99799d-c26c-3677-ab2d-9f87751b4596 | -5.60243 | -45.37605 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d84cb04-a44e-3044-bf2c-62a1731d13c9 | -5.74619 | -44.98223 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 622c4ce4-ebf9-3f2d-9684-ad84e7360a99 | -9.69344 | -48.93866 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a25b27f3-2661-3ff7-b5e2-abd894cb2018 | -9.03208 | -45.52502 | 2025-09-26 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5b4f4a2-24dd-317f-8c5e-2b3f59995607 | -8.66673 | -43.99847 | 2025-09-26 04:42:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3348a2a-aefa-3633-99ca-723c3faa77f5 | -5.45917 | -43.06655 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f31b4d73-033f-3c2a-9a19-301c29fcb7cd | -6.99077 | -44.84835 | 2025-09-26 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35340b77-a9f3-37a4-98a7-b2c6b2ef730c | -7.48565 | -43.89106 | 2025-09-26 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f42d46a5-d61f-3ca0-807a-1cdf9e9b43a3 | -6.25689 | -42.47755 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7088b555-c9a4-39b3-b38a-967d87a84a56 | -10.39872 | -46.14243 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 168cb1c1-10e4-3e2b-b968-382dd11cfaa5 | -5.73352 | -44.96063 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c957ff5a-23c4-3b04-b020-dd356a268c4d | -9.55067 | -47.5234 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11902c89-54f3-3d54-aac3-668504e6cfa0 | -6.99807 | -46.99021 | 2025-09-26 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc892603-a0b0-363d-ae8a-656302a8a275 | -7.77461 | -47.39847 | 2025-09-26 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1989742-d121-3b3a-a50d-2b5fde1a628b | -7.67856 | -45.98756 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7fdd102-75ee-34e6-a0ba-a31857bfcd72 | -3.81065 | -52.08241 | 2025-09-26 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da6d758-2a22-37b3-a83d-5534ed389f15 | -5.24182 | -43.08446 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f013664-a01f-39e6-a4c8-1807819928b6 | -7.00393 | -46.99915 | 2025-09-26 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49d993e9-91cd-3817-a775-deb44b0e2382 | -9.48823 | -40.35733 | 2025-09-26 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20bd178c-be94-3611-952f-52aa055d400b | -5.638 | -43.93111 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d1f35c31-d9e3-3a32-bbf5-61d5b8f4af12 | -10.40301 | -46.16748 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44c13255-f57b-3225-b39c-17c94f565a9f | -10.39554 | -46.13708 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11ce0cfd-31f6-3b94-ae01-9091d5fb91ae | -4.26703 | -48.55148 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 244d9bce-d876-30dd-9577-d8e831cd2b8b | -7.66629 | -47.42237 | 2025-09-26 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98ef79c3-f7ad-3b5d-ba97-7daca11e5539 | -4.27728 | -48.18175 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2222aadb-e65f-3111-a4d6-e46196cd3657 | -6.25554 | -42.48683 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bd89734f-caa9-3182-bb75-26b967b03454 | -7.79823 | -46.01255 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85d2be92-b641-3d2c-9849-b8299bf8da59 | -7.30841 | -45.75995 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d82df712-29b0-3e15-a229-5cd2c181f184 | -7.66972 | -45.99541 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d99599ed-f2ac-3765-a9fe-dd5d5b3c2e5d | -10.11888 | -45.30588 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29f744ea-29f6-306e-bb9c-6182ef2b5815 | -7.68231 | -45.98814 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6055ab4c-2b3e-3de1-b329-803d5880adeb | -9.94851 | -46.27774 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 015607e7-0625-3c0d-a15d-e16208389c05 | -5.54085 | -42.815 | 2025-09-26 04:42:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a5c5bc74-7bc1-3909-91ec-4b915eaf18d2 | -10.93124 | -42.78898 | 2025-09-26 04:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ab94812-055b-323d-81ab-46d137ad0f07 | -7.59921 | -44.43142 | 2025-09-26 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| accd3238-4448-38a9-9618-3722ef52b731 | -6.85396 | -43.19226 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ddc6c596-7284-3e1e-bae6-34f5cceee64a | -5.31848 | -43.13844 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8de33e6a-c83e-37ea-9798-23d0bc7c7b9b | -6.55878 | -43.52837 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ce89a19-889a-369c-be36-505afc5abbd5 | -5.46436 | -43.06393 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d507c86a-c398-3552-bdc9-a97f57a36cea | -10.29201 | -45.22608 | 2025-09-26 04:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60509067-a73a-3caa-8ae4-a9ca56837460 | -7.11072 | -43.7406 | 2025-09-26 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24a5b321-b721-3019-b5a3-9e46e26507d4 | -5.46917 | -43.05936 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd0e02c3-6616-30cc-b5f2-839b1d8e89a1 | -8.71363 | -50.05507 | 2025-09-26 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 884a2a6d-6706-3562-890d-094496385a39 | -9.79922 | -47.76713 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddb34467-1e57-3f77-bc5d-380233efbe20 | -9.72228 | -48.2715 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ada0799-80bf-3938-a4da-2a3da25d83db | -8.07678 | -55.22186 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42f4f04e-c08f-3f21-93f4-25c15c11dc60 | -6.5336 | -44.33403 | 2025-09-26 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74d93fc9-11e9-3739-a55b-7d550603e363 | -5.75149 | -44.9733 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3a2023f-c803-3f6c-8f68-bb770bb7988b | -5.3923 | -45.85299 | 2025-09-26 04:42:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a9b4307-f415-38ae-8178-3eae2bcd01e9 | -7.10643 | -43.73994 | 2025-09-26 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c62f8941-7cd9-3976-81e5-e844dd7bf0a6 | -10.40685 | -46.1681 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3342df5-6162-3fa3-bdea-1662204d3818 | -5.73454 | -44.98055 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8f9f44cc-641b-3758-97f1-0e452a1914ea | -9.76074 | -49.3134 | 2025-09-26 04:42:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 827c366e-fecc-34da-aadb-a9958347072f | -8.4969 | -49.54422 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e4b681-017f-300a-b9ba-e6353e3ea1cd | -9.87216 | -45.91091 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06e82caf-aa62-3421-a6c1-4ee53111c4be | -5.58363 | -48.95345 | 2025-09-26 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc5f621a-c088-396e-b83b-1ac257eb8189 | -7.81718 | -46.90037 | 2025-09-26 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0f9a16-d6dd-3343-af5c-9244ff59aeea | -5.74141 | -42.55996 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fdca9512-62a6-3940-bbfc-bc55e0a044fa | -8.13069 | -42.38033 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3673cf20-7c48-3a16-b3a4-654c574735b8 | -7.67346 | -45.99598 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 842cc414-016a-3341-bfc6-04dfc1e2c3c5 | -5.14915 | -44.51548 | 2025-09-26 04:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15aa50ff-6fc6-3209-bc55-5214ad952b6a | -7.31011 | -45.77424 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3defe15a-c454-37ab-870f-f98c9c31f2d8 | -5.63913 | -43.92364 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd7e803e-dc99-3ce0-8917-47569a94c02b | -5.78722 | -43.82968 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fad042c-6bb1-392c-acad-a48aa8f88da2 | -9.24841 | -44.2657 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b3ecbb7-0203-3cec-877c-037e4037da96 | -10.40753 | -46.1633 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47475d1c-9862-379c-bfa8-9674cfdc1ded | -9.24397 | -48.56305 | 2025-09-26 04:42:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dabd4c03-0674-31e9-b1a0-57de1bfb6144 | -5.22926 | -46.09349 | 2025-09-26 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24cb14a4-b0bd-32c2-934c-264276a9aa2b | -4.74895 | -43.60742 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 407f3901-9ad3-3e45-8e4d-d0cf83bb762b | -9.80354 | -45.72464 | 2025-09-26 04:42:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39f95cd6-0573-31a8-86ce-de125e18624b | -7.63572 | -47.69156 | 2025-09-26 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
