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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5476e7d-3783-3ebf-94db-2750aba8f0e1 | -12.5236 | -58.3576 | 2025-06-07 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| cfc9fde6-d86b-3881-bf2b-5162cfb079b1 | -6.9414 | -42.907 | 2025-06-07 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| e72ae47e-5d45-3cca-a417-a036794e8f29 | -7.7361 | -44.1823 | 2025-06-07 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 15c9c04e-7f86-3441-b529-28c6cb8d6d9c | -6.2228 | -43.3226 | 2025-06-07 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| c872166f-3762-3e15-ac70-4bc9c7edaaa9 | -11.3716 | -56.558 | 2025-06-07 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8aa0c654-93db-30dd-a8c4-080693224113 | -7.0169 | -44.5954 | 2025-06-07 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 26f83c2a-6131-308b-b77e-ff7ab44cebe9 | -6.1853 | -43.3257 | 2025-06-07 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 5986e60e-8402-3456-b509-451e85e8ecda | -11.2736 | -60.7945 | 2025-06-07 00:00:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6d2bb8ba-0310-3a3a-809d-5f0faccfc20a | -7.7173 | -44.1842 | 2025-06-07 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7c62961a-1313-3367-80c0-f2fe8f640de0 | -6.9605 | -42.8816 | 2025-06-07 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 5f403349-5dc0-3112-9327-ca81c231abf4 | -6.204 | -43.3241 | 2025-06-07 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 44eae7f0-0b5d-3d17-95e2-9128b776cccb | -5.6567 | -43.7161 | 2025-06-07 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 84321ba2-e88a-3596-8e76-228d5b030569 | -13.4733 | -56.8557 | 2025-06-07 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 99aa31bc-8660-3e5b-bfd2-d94a8cda5516 | -5.6379 | -43.7175 | 2025-06-07 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ef82680a-b7a6-352f-a252-bc65a6fe58f4 | -6.9791 | -42.9034 | 2025-06-07 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 1785e2d7-c8c6-34b3-8d7c-369540f3649f | -6.2038 | -43.3475 | 2025-06-07 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 414bdc07-ef8f-3c46-b160-dcb71bbe47e5 | -6.96 | -42.9288 | 2025-06-07 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| e893ec83-6dc8-3085-b2a9-d9bbd73903a4 | -7.7176 | -44.1611 | 2025-06-07 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.5 |
| f4aa8456-d6e6-3053-9de2-97f554450beb | -11.7826 | -47.402 | 2025-06-07 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 91331dca-1bb5-3085-95ac-9692d349679d | -6.9602 | -42.9052 | 2025-06-07 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| d5e3eb51-aa92-35c7-bd50-70c36dbeab89 | -12.5238 | -58.3378 | 2025-06-07 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6b22be92-2fd1-31dd-8a30-3ffb18df026c | -7.7364 | -44.1592 | 2025-06-07 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2083591b-6052-34f9-84c0-3c4f7bff5519 | -12.5425 | -58.3561 | 2025-06-07 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| d719af36-5a41-340b-8fbc-353153759fb4 | -11.2548 | -60.7957 | 2025-06-07 00:00:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 882eb427-8172-3265-9f9c-a4fa6896432d | -6.1853 | -43.3257 | 2025-06-07 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 324731b9-a84e-3faa-96b9-0da88285365c | -12.5238 | -58.3378 | 2025-06-07 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 55b965b7-2a63-3e61-8a81-ff8fe1b991e5 | -6.9602 | -42.9052 | 2025-06-07 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 5dc8db99-59d0-3ed3-8015-b5339258c66a | -6.204 | -43.3241 | 2025-06-07 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 0b1de011-389e-3775-bbc0-5223d9e1c2c8 | -7.7361 | -44.1823 | 2025-06-07 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 29f266e5-ce70-30b4-a762-e4d9df01a806 | -11.7826 | -47.402 | 2025-06-07 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d9b4368d-ef3d-3021-9c59-2c716ba386da | -7.7173 | -44.1842 | 2025-06-07 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 178b3c69-fb04-3827-8da7-d49766efcfea | -6.2038 | -43.3475 | 2025-06-07 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6aa9e6eb-80c2-36be-97e2-e9ca1a38e1fa | -7.7176 | -44.1611 | 2025-06-07 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c2433311-6cac-3a27-affd-6aaa7fdc3ef9 | -13.4733 | -56.8557 | 2025-06-07 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0f72a186-5dff-3c62-9c0f-47251bb3de30 | -7.7364 | -44.1592 | 2025-06-07 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a64fe6eb-ea59-3b56-835e-19be501a67b5 | -6.9414 | -42.907 | 2025-06-07 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 2f75f384-eccc-3874-8508-3212dd94fcc9 | -11.2548 | -60.7957 | 2025-06-07 00:10:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 71059561-dc3b-3cbf-a90f-7dead2eafc98 | -12.5236 | -58.3576 | 2025-06-07 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 95c03b4a-1fdc-3ba3-855a-e37360a2896a | -6.9605 | -42.8816 | 2025-06-07 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.1 |
| e3bbd72a-2dae-35b8-a145-89d377bf3eb4 | -22.56888 | -42.16636 | 2025-06-07 00:16:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 703716db-5db6-3fe8-89df-6cb1a5da2e91 | -16.06437 | -43.65966 | 2025-06-07 00:18:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 535e93fc-e6e6-31e6-b455-e9e8b172f0dc | -14.50206 | -43.80535 | 2025-06-07 00:18:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fdf9c9d2-a463-39b3-b459-4d26ee261fca | -15.91205 | -43.46433 | 2025-06-07 00:18:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14dbbf27-4af1-3520-9940-5ed59795516d | -17.25844 | -42.659 | 2025-06-07 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c490953a-4733-3110-88e1-856e439590e5 | -14.50336 | -43.81545 | 2025-06-07 00:18:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ace8af65-e579-3343-939d-29569cc43378 | -14.90046 | -46.02373 | 2025-06-07 00:18:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f4760e80-4112-392f-9e75-e34f672f378e | -17.26751 | -42.65766 | 2025-06-07 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b07c6663-3415-3e8e-b5ab-f46666c7fad6 | -14.73355 | -45.07884 | 2025-06-07 00:18:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 86b4edf7-5a66-3836-9e53-d24abc51f294 | -14.81871 | -40.78508 | 2025-06-07 00:18:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f80c0dea-9f16-3fe1-874e-c26e467a18fc | -6.2038 | -43.3475 | 2025-06-07 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2eb47201-06ff-360c-9a2b-97a301fc9eda | -13.4733 | -56.8557 | 2025-06-07 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d7aa26b2-2aba-3fe1-ad7b-18f8c168a2b8 | -7.7364 | -44.1592 | 2025-06-07 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| e6c6e84d-62ce-30c0-8067-d5ef1745245c | -7.7176 | -44.1611 | 2025-06-07 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 16033516-83f8-36e5-aba8-e923a34e546f | -7.7173 | -44.1842 | 2025-06-07 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6b68a600-a56f-3b89-bdd6-15bd6530a524 | -6.9602 | -42.9052 | 2025-06-07 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 183.5 |
| 6d6d1b4e-c524-300e-8a3f-5ebddff09b04 | -11.2548 | -60.7957 | 2025-06-07 00:20:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f73a41d8-a5bf-3353-a5df-1bbdce15a5b5 | -12.5236 | -58.3576 | 2025-06-07 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 283373fa-cbc7-3996-b548-d7955e3ab93f | -13.4542 | -56.8575 | 2025-06-07 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 02eafbce-c16c-38ac-a0ed-e4fdb2e92a3b | -11.818 | -44.2703 | 2025-06-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 653d8ef5-6f23-3636-89a9-af5e4a0323e2 | -6.204 | -43.3241 | 2025-06-07 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 78603a90-5ecc-34ca-8440-170ad99278b9 | -7.0169 | -44.5954 | 2025-06-07 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 607bedcf-0f1b-378e-8258-9c8eddbc884b | -12.5238 | -58.3378 | 2025-06-07 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3b93f766-b0a9-3e8b-8542-4ca5aba6a692 | -9.3972 | -48.4305 | 2025-06-07 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| eb406d82-fb89-3569-a69c-0aa2ea9ce5e8 | -6.96 | -42.9288 | 2025-06-07 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| cd67e5b6-2cd2-3635-a6f1-a1c303c215d2 | -6.9605 | -42.8816 | 2025-06-07 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| ccf10d93-de48-3d70-a46b-f141a4411c3f | -11.7826 | -47.402 | 2025-06-07 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 913b6ed1-67a0-3177-a175-1cce223996c3 | -7.7361 | -44.1823 | 2025-06-07 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9da20a6b-d767-386c-8ff7-7f22b53256fa | -12.5425 | -58.3561 | 2025-06-07 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| ccd774ad-4d9c-3be1-b250-9af21b7fcf44 | -6.9414 | -42.907 | 2025-06-07 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 2a051ac7-0830-37db-94a9-dc5162f10530 | -6.66856 | -47.72933 | 2025-06-07 00:20:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 91832f3c-352c-3c4e-9774-ae280983eb21 | -11.82186 | -44.26021 | 2025-06-07 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bd86da7d-5685-3aff-96e7-06b47755ae25 | -10.7105 | -48.78843 | 2025-06-07 00:20:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| afffeca5-1de2-3e05-b980-61b72b502b66 | -12.53208 | -45.4117 | 2025-06-07 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6d9df077-7434-3c57-bec2-1ef1e85826fc | -11.82316 | -44.27007 | 2025-06-07 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e570052b-8288-3a69-8119-68eb8bd9c4e2 | -6.95698 | -42.90149 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| e97fa4db-12fa-367f-be18-bb9800f40348 | -5.7745 | -43.61457 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6b4d6d1a-f3bf-3de3-876c-66de1f1b1117 | -9.40284 | -48.42846 | 2025-06-07 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 14c6a47e-7160-3970-b25e-37f5f997b7e2 | -6.94815 | -42.90275 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 1bc87f27-f893-361b-a216-dfe304a87891 | -9.40492 | -48.44553 | 2025-06-07 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 02712f03-a8c4-3316-b87b-cf21f71822ca | -12.96472 | -46.76702 | 2025-06-07 00:20:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b99d97ff-a11b-354a-b511-a02d5b23ef83 | -6.94331 | -42.80371 | 2025-06-07 00:20:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2d838133-6578-3701-9d19-4de3fe3849a9 | -6.19674 | -43.33538 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| bab9d7fe-728d-31cd-86b9-11e2727797ae | -7.00906 | -44.61449 | 2025-06-07 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5da28a81-9171-3fe5-bce1-7612894115f6 | -13.33722 | -45.48943 | 2025-06-07 00:20:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 13210083-a2de-35ad-807a-214004d5f161 | -9.33385 | -48.5133 | 2025-06-07 00:20:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 58598f68-7532-3165-b01b-77d04d00dec6 | -6.94939 | -42.91163 | 2025-06-07 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 3d62775e-515d-389e-8928-9034960e34d5 | -9.50043 | -40.31731 | 2025-06-07 00:20:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bfb91044-a065-36ab-a95b-b58e373ea1c6 | -6.21164 | -44.50531 | 2025-06-07 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f9bbe723-47bf-313d-94b9-15907747b5ba | -12.32907 | -52.47546 | 2025-06-07 00:20:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 413349ae-1616-354a-9b4b-7a64318c11f7 | -12.41656 | -43.81733 | 2025-06-07 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b37736d5-f89a-30d1-92e6-a6ada535970e | -8.44617 | -46.48882 | 2025-06-07 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d08428bd-0b6d-38ca-adf3-998727c29624 | -11.78496 | -47.41732 | 2025-06-07 00:20:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f890038b-6c91-303b-89bb-95ee023c84ca | -8.21551 | -48.98444 | 2025-06-07 00:20:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 33.6 |
| adc57c43-7717-370f-a2e5-bafcdf933b5b | -14.23514 | -45.48895 | 2025-06-07 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7de29437-c9a4-3983-88f5-d6792f8fab52 | -5.64189 | -43.71101 | 2025-06-07 00:20:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d11e6cb6-2668-3d91-aafa-a0e65e5d8024 | -6.20433 | -43.32532 | 2025-06-07 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 2482f450-6e56-3f50-9f7e-02e8f0e6ad0b | -6.54015 | -45.69783 | 2025-06-07 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e93e0c86-3f96-373e-9a75-8f2c8aa2170a | -11.78303 | -47.40165 | 2025-06-07 00:20:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 3881242f-072b-303c-9c9e-bb206e715f90 | -8.17306 | -46.50874 | 2025-06-07 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 51a5da37-8caf-3695-8a37-964a9e929a31 | -7.74225 | -44.17761 | 2025-06-07 00:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README2.md)
