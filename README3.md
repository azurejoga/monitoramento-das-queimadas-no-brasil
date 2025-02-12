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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e0059a8-b798-3adc-9e41-1569e353667e | -21.52081 | -47.16387 | 2025-02-12 04:04:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99ee1e6-e44a-3f31-b95f-be8cb1e3a7c3 | -22.53794 | -48.81391 | 2025-02-12 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3a48dc7-a9cc-3ac9-b962-99b630537e21 | -22.8411 | -42.78834 | 2025-02-12 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 53ff0962-e03f-30e1-8ab8-6989f8342c7a | -21.37846 | -49.15631 | 2025-02-12 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bdb3a2b-45e9-365c-91b8-b6b75b5b6567 | -20.21694 | -46.43404 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c112f00-0fce-31d1-8936-8b68bc482f54 | -21.27629 | -48.57529 | 2025-02-12 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86f6725-0c11-3f1d-bbc5-eb0d790cb668 | -21.27382 | -48.98149 | 2025-02-12 04:04:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fe1254a-f3c7-32cd-b632-3449b3ba6789 | -22.67537 | -42.8577 | 2025-02-12 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3899e1d4-2529-3586-8182-255adb984821 | -20.21619 | -46.43833 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89566f4d-877d-34de-a5aa-5520cdaf4f6e | -22.78324 | -43.4136 | 2025-02-12 04:04:00 | NOAA-20 | MESQUITA | RIO DE JANEIRO | Brasil | 3302858 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09201b9f-8244-3d0e-9d0a-88335909f6c1 | -23.43093 | -46.75838 | 2025-02-12 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a0267a0-ff46-3781-a68b-534df865490b | -22.92107 | -45.41475 | 2025-02-12 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 671bbc6c-e659-300c-821a-a1d8589c73f6 | -22.90324 | -43.75368 | 2025-02-12 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 482fbf06-fc0e-3dee-9f41-01649134f9e8 | -21.27803 | -48.57365 | 2025-02-12 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0310ad3-2ab5-3d4f-b35d-85ad756689d2 | -23.28058 | -46.60144 | 2025-02-12 04:04:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 440fd801-d243-3a0a-826d-5c077bc3ba4d | -21.37933 | -49.15694 | 2025-02-12 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 786137c9-af93-316c-90ac-4c40d5fb7f82 | -22.561 | -47.32034 | 2025-02-12 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed8b3c79-a5d0-3b38-91c4-1ee646f5506b | -23.33772 | -46.77107 | 2025-02-12 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 263f4e96-257f-3161-bc99-e1178b1a3736 | -21.27787 | -48.9823 | 2025-02-12 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea2795c-e522-36c8-b73d-d4faa05e94f4 | -20.21828 | -46.44756 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3796da0f-dbe4-3b61-92a2-d96acf08e574 | -23.9838 | -48.91666 | 2025-02-12 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9359253c-999a-332a-9a3f-fb9f117ae6ed | -21.06757 | -41.58823 | 2025-02-12 04:04:00 | NOAA-20 | BOM JESUS DO NORTE | ESPÍRITO SANTO | Brasil | 3201100 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a19bbc9-67fc-3ae2-9ed7-6fcb12849e20 | -20.21903 | -46.44326 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d458adb0-104c-3199-a295-c81f04e25047 | -21.58091 | -47.0383 | 2025-02-12 04:04:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eed9231-aaa8-3624-a620-ff18752daaae | -20.41794 | -43.55426 | 2025-02-12 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e41e706-bca8-3dc5-8886-abfa5d937107 | -20.22187 | -46.44822 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 597b8230-16bd-3f1b-8b1d-4f8576b55bdf | -23.59392 | -47.43738 | 2025-02-12 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f02620d5-1e10-33d9-9a51-ec58ac0a8046 | -20.21335 | -46.43341 | 2025-02-12 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63f80cd7-a0d3-3ee5-967a-a37deea7a66c | -21.07366 | -56.39166 | 2025-02-12 04:04:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33adf92a-86c6-3584-85ec-5a92b6525182 | -22.81808 | -43.3428 | 2025-02-12 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 625ef3e0-7bd4-355b-b0fa-f5f2f44b69f4 | -22.67594 | -42.85391 | 2025-02-12 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5befe00b-7f8a-3453-b229-d27d357c3718 | -20.71267 | -41.88423 | 2025-02-12 04:04:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| dc2c2c87-b2f1-35b7-9726-cf0da2cff97c | -22.5388 | -48.81298 | 2025-02-12 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bcc6475-8782-38f1-9aec-0b18be93ac08 | -22.67825 | -42.85403 | 2025-02-12 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d781a6a7-7a40-3443-bbd6-838513103b49 | -23.40473 | -46.55719 | 2025-02-12 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cc22a59-a043-323b-bc99-7fbe7479def5 | -23.22692 | -45.60765 | 2025-02-12 04:04:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8be6b06a-5c06-3d33-84ed-8eee281e3f5e | -27.6869 | -48.75096 | 2025-02-12 04:06:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2cf878e1-b954-35f5-ad2a-efe472aacf01 | -29.79135 | -57.11061 | 2025-02-12 04:06:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 78b743f7-71ea-35a1-a288-496f717a5d55 | 4.62717 | -60.64909 | 2025-02-12 04:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59286fd6-a4c1-31b8-9f84-a369243a5ecc | 4.62771 | -60.65284 | 2025-02-12 04:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0159d7bf-56b5-36eb-b83c-d21dd6d90cea | 4.6343 | -60.65705 | 2025-02-12 04:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a035ce59-a7e9-30d4-9521-8ae3df83a1c7 | 1.12304 | -60.52711 | 2025-02-12 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8fa804d6-57f1-370f-9048-a9354b268189 | 1.12359 | -60.53076 | 2025-02-12 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0c119a1-3613-3d3c-8fcc-fa9c6fd6d79f | 3.08165 | -60.02806 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24e3e2d9-1bc6-3e8c-ae48-58e2bbdc8a14 | 3.07168 | -60.03681 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a29924-1555-34cc-b369-980f44d38bb5 | 3.08091 | -60.02642 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a7e2074-de0a-338d-a025-f1e416776fd4 | 3.07595 | -60.03077 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8932384d-fbab-37c0-b38c-a7aac43249fe | 3.07719 | -60.03606 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7f25cc-5855-395b-bef1-2a450ff64bac | 3.07667 | -60.03244 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cef92adf-f681-3bf2-888b-9acf04507681 | 3.07154 | -60.03873 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88a6ce74-07b3-355f-9d87-6b4393483f31 | 3.07705 | -60.03798 | 2025-02-12 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6dc697b-d8db-3293-afe2-bf761548b6fc | -10.536 | -44.67228 | 2025-02-12 04:53:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801a464b-2954-344c-bc7b-9ae8cb220687 | -10.5352 | -44.67862 | 2025-02-12 04:53:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bea9c5a-31dd-34af-a35f-270ba77ab108 | -16.3524 | -43.69587 | 2025-02-12 04:53:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c418b6c-f6a0-3c0c-81ed-3905ed4ae357 | -16.08902 | -60.0598 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ad0483d-c10e-32a1-8b3b-fc462e9823e4 | -16.0837 | -60.06632 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 613197fd-2032-338e-928d-3b95a99fc1c0 | -15.40367 | -59.41501 | 2025-02-12 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 765ca9d3-faf8-3d99-a88b-8ccabda1e2c1 | -17.67511 | -54.16951 | 2025-02-12 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3fcc7105-da85-3382-a0e8-66ed2c3216e9 | -15.39242 | -60.17968 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7a5203c-d7c6-37f2-a6cd-3efcf92bedc2 | -6.97851 | -42.81525 | 2025-02-12 04:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b1b5768-96a5-3bae-8d50-7a7ed80a38cb | -6.978 | -42.81901 | 2025-02-12 04:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe5925da-3563-3f23-97e4-8940a7e5d5f5 | -16.08837 | -60.06345 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e718a52b-e25e-3499-95ca-25d739a8ed74 | -12.83897 | -47.8542 | 2025-02-12 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21939433-9ffe-3d7c-bf7a-dbfe4699384f | -17.67566 | -54.16584 | 2025-02-12 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 150b5f60-8f0e-3252-ac34-410e9675ef15 | -16.08304 | -60.07001 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7814b52f-278a-3547-9901-f31fe3a6bc9e | -16.46473 | -58.16853 | 2025-02-12 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d54a73ab-0f5e-369b-b726-b3b439c6c963 | -10.5356 | -44.67545 | 2025-02-12 04:53:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05aa65fd-ac05-3240-90a3-a1ea047a459f | -9.09926 | -39.96701 | 2025-02-12 04:53:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f4aff2b6-1669-3cf0-a3b1-1437428ac174 | -16.085 | -60.05903 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53348aef-2e88-3aad-84a6-0292c51f51a7 | -15.27231 | -60.31238 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d2c538-727c-3fd2-9c30-61c8dff7edd9 | -6.15589 | -44.75215 | 2025-02-12 04:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 939f2189-172a-3b42-9004-4a67ed281ba8 | -16.25083 | -59.60415 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 154b2882-eb79-3ec8-843e-2f02cd43234a | -16.08238 | -60.07371 | 2025-02-12 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d09d37cd-341c-33ac-914a-b61acf5ebf68 | -20.91314 | -56.53385 | 2025-02-12 04:55:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8195ef3-e399-34e1-a3b2-f08752933ca9 | -19.5507 | -55.08666 | 2025-02-12 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8a1b3d33-5e0a-3930-9a8c-95694510cf49 | -21.27817 | -48.98248 | 2025-02-12 04:55:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b77df607-11cd-3f20-90e2-4134d9ed6466 | -21.87787 | -56.2645 | 2025-02-12 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3d50097-ec20-37e3-866d-e9c4631afefe | -23.22917 | -53.08246 | 2025-02-12 04:55:00 | NOAA-21 | SANTA MÔNICA | PARANÁ | Brasil | 4123956 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89cf961f-568f-38dd-a2de-e2b21d9b3786 | -21.87729 | -56.2682 | 2025-02-12 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93db822d-8b32-33e1-8557-04315146168a | -21.96574 | -57.58568 | 2025-02-12 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c35f480f-caa6-36ce-ab5b-4f7f04c14904 | -22.02022 | -57.12407 | 2025-02-12 04:55:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b2ead0a-d1d1-396a-8b57-6b6f4846e69a | -22.53995 | -48.81308 | 2025-02-12 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df68c207-3741-30a1-b6fe-7e5d5be96963 | -20.90924 | -56.53694 | 2025-02-12 04:55:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae11d972-9b4d-3404-b5c4-bde28247daca | -20.91645 | -56.53444 | 2025-02-12 04:55:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6bfa8a2-a751-36f6-8272-f0e4cb66e6b2 | -21.07848 | -56.3925 | 2025-02-12 04:55:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 992c9fd0-2f0e-3d62-b107-039daa208e07 | -22.53893 | -48.81358 | 2025-02-12 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45292965-7bc5-339a-939c-7f25cc504019 | -13.24782 | -48.41451 | 2025-02-12 04:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeabaac0-a755-3f65-9b2d-c9b37fab5b4c | -21.83003 | -56.50367 | 2025-02-12 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 925ac37b-91b9-3cd3-b3cd-4d55560b5bba | -21.07906 | -56.38881 | 2025-02-12 04:55:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1b633aa-bc06-3ac8-b696-a3ab3fc5ebca | -21.41875 | -48.55221 | 2025-02-12 04:55:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f5d541b6-6ff2-3335-8a00-507b28017ff7 | -21.96511 | -57.58952 | 2025-02-12 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 992be997-66ea-397d-9de5-17d7b46b0d1d | -29.79197 | -57.11017 | 2025-02-12 04:57:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 74b81ecc-b079-3786-9172-cad4d05b2379 | -29.81409 | -55.99405 | 2025-02-12 04:57:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 6c7c52c2-07cf-32fa-a8cf-1b919b4a0404 | -29.79532 | -57.11081 | 2025-02-12 04:57:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| a78f6b2c-1033-376e-8fb3-8f94783c7728 | -29.81753 | -55.99467 | 2025-02-12 04:57:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a28a6117-b43d-326a-b65d-672f64428bc6 | 4.63486 | -60.64955 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb22d99-3cab-3ce5-8e36-88a1367240cf | 4.6248 | -60.66016 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7611795-ecae-3917-9550-8e3843813094 | 4.62721 | -60.65043 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389787d3-e11c-31a9-b2c1-1f763c64bf8d | 4.63103 | -60.65 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66f3310e-09ba-3573-ad7d-25d27c22391a | 4.62861 | -60.65962 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
